import numpy as np
import pytorch

class Network(object):
    """docstring for Trainer"""
    def __init__(self):
        super(Trainer, self).__init__()
        pass
        
    def train(self):
        pass

    def predict(self):
        pass



class ExpReplay(object):
    def __init__(q_size):
        self.q = []
        self.n = q_size

    def add(self):
        pass

    def remove_from_q(self):
        pass

    def sample(self, sample_size):
        pass

    def self_balance(self):
        pass
