import time

from src.player import Player


class Game(object):
    player = None
    hour = 0
    ending = None

    def __init__(self):
        print("Добро пожаловать на выборы! ")
        self.player = Player()
        self.player.start()
        self.run()

    def run(self):
        while self.ending is None:
            self.step()

    def step(self):
        print("День {}, {}:00".format(1 + self.hour // 24, self.hour % 24))
        if not self.get_event():
            print("Ещё один скучный час\n")
        self.hour += 1
        time.sleep(0.5)

    def get_event(self):
        fun = False
        self.player.stop()
        for event in self.player.events:
            if self.hour in event.range:
                mins = event.conditions.get('min', {})
                maxs = event.conditions.get('max', {})
                past = event.conditions.get('events', {})
                condition_min = not mins or all([self.player.parameters[key] >= value for key, value in mins.items()])
                condition_max = not maxs or all([self.player.parameters[key] < value for key, value in maxs.items()])
                condition_past = not past or all([event in self.player.past_events and
                                                  self.player.past_events[event] == choice
                                                  for event, choice in past.items()])

                result = None
                #print(condition_past, condition_max, condition_min)
                if condition_min and condition_max and condition_past:
                    result = event.dispatch()
                if result is not None:
                    if event.type == "ending":
                        self.ending = True
                        return
                    choice, reaction = result
                    self.player.add_past_event(event_name=event.name, choice=choice)
                    self.player.apply_reaction(reaction=reaction)
                    fun = True
        self.player.start()
        return fun

game = Game()
