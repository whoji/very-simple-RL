import numpy as np
import pytorch


class Network(object):
    """docstring for Trainer"""
    def __init__(self, n_feature, n_hidden_l1, n_hidden_l2, n_output):
        super(Network, self).__init__()
        
        self.l1 = torch.nn.Linear(n_feature, n_hidden_l1)
        self.l2 = torch.nn.Linear(n_hidden_l1, n_hidden_l2)
        self.out = torch.nn.Linear(n_hidden_l2, n_output)
       
    def forward(self, x):
        a1 = F.relu(self.l1(x))
        a2 = F.relu(self.l2(x))
        o = self.out(a2)
        return x
        
    def train(self):
        pass

    def predict(self):
        pass

class Trainer(object):
    def __init__(self, x, y):
        self.net = Network(2, 10, 10, 3)
        self.optimizer = torch.optim.SGD(net.parameters(), lr=0.02)
        self.loss_func = torch.nn.CrossEntropyLoss()
        self.x = x
        self.y = y

    def train(self, epochs = 100):
        for t in range(epochs):
            out = self.net(x)
            loss = self.loss_func(out, y)

            optimizer.zero_grad()   # clear gradients for next train
            loss.backward()         # backpropagation, compute gradients
            optimizer.step()        # apply gradients


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
