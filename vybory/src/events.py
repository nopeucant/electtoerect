# -*- coding: utf-8 -*-
import random


class Event(object):
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.name = data.get('name', '')
        self.type = data.get('type', '')
        self.probability = data.get('probability', 0)
        rang = data.get('range', (0, 1))
        self.range = range(rang[0], rang[1])
        self.real_probability = self.probability/len(self.range)
        self.text = data.get('text', '')
        self.actions = data.get('actions', [])
        self.reactions = data.get('reactions', [])
        self.action_conditions = data.get('action_conditions', [])
        self.conditions = data.get('conditions', {})
        self.recently_happened = False
        self.repeatable = data.get('repeatable', False)

    def dispatch(self):
        happens = random.random()
        if happens > self.real_probability:
            return None
        print(self.text)
        for i, action in enumerate(self.actions):
            print("{}. {}".format(i+1, action))
        answer = None
        while answer is None:
            answer = int(input())
            if answer-1 < len(self.reactions):
                return answer, self.reactions[answer-1]
            else:
                print("Ха-ха, очень смешно.")
                answer = None
