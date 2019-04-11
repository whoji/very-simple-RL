import numpy as np
import torch
import torch.nn.functional as F


class Network(torch.nn.Module):
    """docstring for Trainer"""
    def __init__(self, n_feature, n_hidden_l1, n_hidden_l2, n_output):
        super(Network, self).__init__()
        
        self.l1 = torch.nn.Linear(n_feature, n_hidden_l1)
        self.l2 = torch.nn.Linear(n_hidden_l1, n_hidden_l2)
        self.out = torch.nn.Linear(n_hidden_l2, n_output)
       
    def forward(self, x):
        a1 = F.relu(self.l1(x))
        a2 = F.relu(self.l2(a1))
        o  = torch.sigmoid(self.out(a2))
        return o
            
    def train(self):
        pass

    def predict(self, x):
        y_hat = self.forward(x)
        return round(y_hat.detach().numpy()[0])

    @staticmethod
    def to_torch_tensor(x):
        return  torch.FloatTensor(x)


class Trainer(object):
    def __init__(self, net):
        if net:
            self.net = net
        else:
            self.net = Network(2, 10, 10, 3)

        self.optimizer = torch.optim.SGD(self.net.parameters(), lr=0.02)
        self.loss_func = torch.nn.CrossEntropyLoss() # MSELoss
        self.x = None
        self.y = None
        self.accuracy = 0.0

    def train(self, epochs=100, verbose=True):
        # assert self.x is pytorch tensor of good shape
        # assert self.y is pytorch tensor of good shape
        for t in range(epochs):
            out = self.net(self.x)
            loss = self.loss_func(out, self.y)

            self.optimizer.zero_grad()   # clear gradients for next train
            loss.backward()              # backpropagation, compute gradients
            self.optimizer.step()        # apply gradients

            if verbose and t % 10 == 0:
                # plot and show learning process
                prediction = torch.max(out, 1)[1]
                pred_y = prediction.data.numpy()
                target_y = self.y.data.numpy()
                self.accuracy = float((pred_y == target_y).astype(int).sum()) / float(target_y.size)
                print('Accuracy=%.2f' % self.accuracy)

    def inference(self, x):
        return self.net(x)


class ExpReplay(object):
    def __init__(self, q_size_max = 1000):
        self.q = []
        self.q_size_max = q_size_max

    def reset(self):
        self.q = []

    def add(self, x, a, r):
        assert len(self.q) < self.q_size_max
        one_data_pt = (x, a, r)
        self.q.append(one_data_pt)

    def sample(self, sample_size = 1):
        # sort the q by the r val, and sample the best ones
        assert sample_size <= len(self.q) 
        sorted_q = sorted(self.q, key = lambda x: -x[2])
        return sorted_q[:sample_size]

    def sample_positive(self):
        ret_x = [d[0] for d in self.q if d[2] > 0]
        ret_y = [d[1] for d in self.q if d[2] > 0]
        #import pdb; pdb.set_trace()
        ret_x = torch.stack(ret_x)
        ret_y = torch.LongTensor(ret_y)
        return ret_x, ret_y

    def remove_from_q(self):
        pass

    def self_balance(self):
        pass

    def data_transform(self, x, a, r):
        #transform into pytorch data
        x = torch.FloatTensor(x)
        a = torch.FloatTensor(a)
        r = r
        return x, a, r


