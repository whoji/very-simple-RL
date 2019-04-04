import numpy as np
import random
from ml_core import Network, ExpReplay

class Agent(object):
    """This is the player"""
    def __init__(self, memory_len, money):
        super(Agent, self).__init__()
        self.episodes = 0
        self.memory_len = memory_len
        self.money = money
        self.queue_self = []
        self.queue_enemy = []
        self.net = Network(memory_len*2,5,3,1)
        self.exp = ExpReplay()

        # initialize the queue
        self.queue_self = [random.choice([-1,0,1]) for _ in range(memory_len)]
        self.queue_enemy = [random.choice([-1,0,1]) for _ in range(memory_len)]
        
    def get_x(self):
        # get the x in good format for network (trainer)
        print(self.queue_self)
        print(self.queue_enemy)
        # raise NotImplementedError
        print(self.queue_self+self.queue_enemy)
        return self.net.to_torch_tensor(self.queue_self+self.queue_enemy)

    def get_action(self):
        # get action from the trainer
        x = self.get_x()
        a = self.net.predict(x)
        return a

    def take_action(self, a):
        # also take the action to the self.queue_self
        # TODO implement this r
        self.queue_self.append(a)
        self.money += 0 # TODO

    def saw_action(self, agent_actions, game_actions):
        self.queue_self = agent_actions
        self.queue_enemy = game_actions

    def need_train(self):
        if len(self.exp.q) == self.exp.q_size:
            return True
        else:
            return False

    def meditate(self):
        # decide if we need to train the model
        # if yes. also train itself during this meditation period

        raise NotImplementedError
        self.exp.add(x, a, r)

        # if need train
        if not self.need_train():
            return 0

        # train the network
        self.net.train()
