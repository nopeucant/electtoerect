import json
import os

from src.events import Event
from src.parameters import ParameterHolder


class Player(ParameterHolder):
    name = 'player'
    events = []
    past_events = {}
    in_progress = False

    def __init__(self):
        self.name = input("Введи имя, кандидат: ")
        self.read_events()

    def read_events(self):
        dir = "events"
        for filename in os.listdir(dir):
            with open(os.path.join(dir, filename), 'rt') as file:
                print(filename)
                data = json.load(file)
                self.events.append(Event(data))

    def start(self):
        self.in_progress = True

    def stop(self):
        self.in_progress = False

    def add_past_event(self, event_name, choice):
        self.past_events[event_name] = choice

    def apply_reaction(self, reaction):
        for param, addition in reaction.items():
            self.parameters[param] += addition
