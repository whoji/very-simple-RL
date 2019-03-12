import numpy as np
from ml_core import Network, ExpReplay

class Agent(object):
    """This is the player"""
    def __init__(self):
        super(Agent, self).__init__()
        self.episodes = 0
        self.money = 0
        self.queue_self = []
        self.queue_enemy = []
        self.net = Network()
        self.exp = ExpReplay()
        
    def get_x(self):
        # get the x in good format for network
        pass

    def get_action(self):
        # get action from the trainer
        x = self.get_x()
        a = net.predict(x)
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

        self.exp.add(x, a, r)

        # if need train
        if not self.need_train():
            return 0

        # train the network
        self.net.train()
