import numpy as np
import random

class Game(object):
    """docstring for Game"""
    def __init__(self, memory_len = 6, money = 100):
        super(Game, self).__init__()
        self.queue_self = []
        self.queue_enemy = []
        self.memory_len = memory_len

        self.money_self = money
        self.money_enemy = money

        # initialize the queue
        self.queue_self = [random.choice([-1,0,1]) for _ in range(memory_len)]
        self.queue_enemy = [random.choice([-1,0,1]) for _ in range(memory_len)]


    def get_action(self):
        a = self.magic_func_2()
        self.queue_self = self.queue_self[1:]
        self.queue_self.append(a)
        return a

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
                activation += np.sin(11*self.queue_self[i])
                activation += np.cos(12*self.queue_enemy[i])
                activation -= np.cos(13*self.queue_enemy[i]+13*self.queue_self[i])
            else:
                activation -= np.cos(14*self.queue_self[i])
                activation -= np.sin(15*self.queue_enemy[i])
                activation -= np.sin(16*self.queue_enemy[i]+16*self.queue_self[i])

        activation = self.sigmoid(activation)
        action = round(activation)
        return action

    def magic_func_2(self):
        activation_0 = 0
        activation_1 = 0
        for i in range(self.memory_len):
            if i % 2 == 0:
                activation_0 += i*self.queue_self[i]
                activation_1 -= i*self.queue_enemy[i]
            else:
                activation_0 -= i*self.queue_self[i]
                activation_1 += i*self.queue_enemy[i]
        activation = abs(activation_0) + abs(activation_1)
        #print(activation)
        return round(activation) % 3 - 1

    @staticmethod
    def sigmoid(x, derivative=False):
        return x*(1-x) if derivative else 1/(1+np.exp(-x))

    @staticmethod
    def get_reward(a,b):
        d = {}
        d[-1] = {}
        d[0] = {}
        d[1] = {}
        d[-1][-1] = 0
        d[-1][0] = -1
        d[-1][1] = 1
        d[-0][-1] = 1
        d[-0][0] = -0
        d[-0][1] = -1
        d[1][-1] = -1
        d[1][0] = 1
        d[1][1] = 0

        return d[a][b]


'''
    |-1  0 +1
 ---+-------
 -1 | 0 -1  1
  0 | 1  0 -1
 +1 |-1  1  0

'''