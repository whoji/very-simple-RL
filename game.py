import numpy as np
import random

class Game(object):
    """docstring for Game"""
    def __init__(self, memory_len = 5, money = 100):
        super(Game, self).__init__()
        self.queue_self = []
        self.queue_enemy = []
        self.memory_len = memory_len

        self.money_self = money
        self.money_enemy = money

        # initialize the queue
        self.queue_self = random.choice([-1,0,1], memory_len)
        self.queue_enemy = random.choice([-1,0,1], memory_len)


    def get_action(self):
        a = self.magic_func()
        self.queue_self = self.queue_self[1:]
        self.queue_self.append(a)

    def saw_action(self, a):
        self.queue_enemy = self.queue_enemy[1:]
        self.queue_enemy.append(a)
        reward = self.get_reward(self.queue_self[-1],a)
        self.money_self += reward
        self.money_enemy -= reward

    def magic_func(self):
        activation = 0
        for i in range(self.memory_len):
            if i % 2 == 0:
                activation += np.sin(self.queue_self[i])
                activation += np.cos(self.queue_enemy[i])
            else:
                activation += np.cos(self.queue_self[i])
                activation += np.sin(self.queue_enemy[i])

        activation = np.sigmoid(activation)
        action = round(activation)
        return actions

    @staticmethod
    def get_reward(a,b):
        d = {}
        d[][] = 1
        d[][] = 1
        d[][] = 1
        d[][] = 1
        d[][] = 1

        return d[a][b]


'''
    |-1  0 +1
 ---+-------
 -1 | 0 -1  1
  0 | 1  0 -1
 +1 |-1  1  0

'''