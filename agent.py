import numpy as np
import random
from ml_core import Network, ExpReplay, Trainer

class Agent(object):
    """This is the player"""
    def __init__(self, memory_len, money, eps, eps_decay, lr):
        super(Agent, self).__init__()
        self.episodes = 0
        self.memory_len = memory_len
        self.money = money
        self.queue_self = []
        self.queue_enemy = []
        self.net = Network(memory_len*2,5,3,3)
        self.exp = ExpReplay()
        self.trainer = Trainer(self.net, lr)
        self.eps = eps
        self.eps_decay = eps_decay

        # initialize the queue
        self.queue_self = [random.choice([0,1,2]) for _ in range(memory_len)]
        self.queue_enemy = [random.choice([0,1,2]) for _ in range(memory_len)]
        
    def get_x(self):
        # get the x in good format for network (trainer)
        return self.net.to_torch_tensor(self.queue_self+self.queue_enemy)

    def get_action(self):
        # get action from the trainer
        x = self.get_x()
        a = self.net.predict(x)
        if random.uniform(0,1) < self.eps:
            a = self.random_action(a)
        self.eps = self.eps * self.eps_decay
        return a

    def random_action(self, a):
        return random.choice([0,1,2])

    def take_action(self, a):
        # also take the action to the self.queue_self
        # TODO implement this r
        self.queue_self.append(a)
        self.money += 0 # TODO

    def saw_action(self, agent_actions, game_actions):
        self.queue_self = agent_actions
        self.queue_enemy = game_actions

    def need_train(self):
        if len(self.exp.q) == self.exp.q_size_max:
            return True
        else:
            return False

    def meditate(self):
        # decide if we need to train the model
        # if yes. also train itself during this meditation period

        x = self.get_x()
        a = self.queue_self[-1]
        r = self.get_reward(self.queue_self[-1], self.queue_enemy[-1])
        self.exp.add(x, a, r)

        # if need train
        if not self.need_train():
            return 0
        else:
            # train the network
            ret_x, ret_y = self.exp.sample_positive()
            self.trainer.x, self.trainer.y = ret_x, ret_y
            # import pdb; pdb.set_trace()
            self.trainer.train()
            self.exp.reset()
            return 1

    @staticmethod
    def get_reward(a,b):
        d = {}
        d[0] = {}
        d[1] = {}
        d[2] = {}
        d[0][0] = 0
        d[0][1] = -1
        d[0][2] = 1
        d[1][0] = 1
        d[1][1] = -0
        d[1][2] = -1
        d[2][0] = -1
        d[2][1] = 1
        d[2][2] = 0

        return d[a][b]
