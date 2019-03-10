import numpy as np
from ml_core import Network

class Agent(object):
    """This is the player"""
    def __init__(self, arg):
        super(Agent, self).__init__()
        self.episodes = 0
        self.money = 0
        self.queue_self = []
        self.queue_enemy = []
        self.net = Network()
        
    def get_action(self):
        # get action from the trainer
        pass

    def take_action(self, a):
        # also take the action to the network
        pass

    def saw_action(self, agent_actions, game_actions):
        self.queue_self = agent_actions
        self.queue_enemy = game_actions

    def meditate(self):
        # decide if we need to train the model
        # if yes. also train itself during this meditation period

        # if need train
        if not self.need_train():
            return 0

        # train the network
        self.net.train()
