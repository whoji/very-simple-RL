import numpy as np
import unittest
import torch
from ml_core import Network, Trainer, ExpReplay

class TestMLCore(unittest.TestCase):
    """docstring for ClassName"""
    def setUp(self):
        self.net = Network(2,4,4,3)
        self.trainer = Trainer(self.net)

        # make fake data
        n_data = torch.ones(100, 2)
        x0 = torch.normal(2*n_data, 1)      # class0 x data (tensor), shape=(100, 2)
        y0 = torch.zeros(100)               # class0 y data (tensor), shape=(100, 1)
        x1 = torch.normal(-2*n_data, 1)     # class1 x data (tensor), shape=(100, 2)
        y1 = torch.ones(100)                # class1 y data (tensor), shape=(100, 1)
        x = torch.cat((x0, x1), 0).type(torch.FloatTensor)  # shape (200, 2) FloatTensor = 32-bit floating
        y = torch.cat((y0, y1), ).type(torch.LongTensor)    # shape (200,) LongTensor = 64-bit integer
        self.dataset = {'x':x, 'y':y}

    def test_network(self):
        self.net = Network(2,4,4,3)
        self.trainer = Trainer(self.net)

        self.trainer.x = self.dataset['x']
        self.trainer.y = self.dataset['y']

        self.assertTrue(self.trainer.accuracy ==  0.0)
        self.trainer.train(1000)
        self.assertTrue(self.trainer.accuracy >  0.9)

    def test_network_multi_class(self):
        # make fake data
        n_data = torch.ones(100, 2)
        x0 = torch.normal(2*n_data, 1)      # class0 x data (tensor), shape=(100, 2)
        y0 = torch.zeros(100)               # class0 y data (tensor), shape=(100, 1)
        x1 = torch.normal(-2*n_data, 1)     # class1 x data (tensor), shape=(100, 2)
        y1 = torch.ones(100)                # class1 y data (tensor), shape=(100, 1)
        x2 = torch.normal(50*n_data, 1)
        y2 = torch.zeros(100) + 2  

        x = torch.cat((x0, x1, x2), 0).type(torch.FloatTensor)  # shape (200, 2) FloatTensor = 32-bit floating
        y = torch.cat((y0, y1, y2), ).type(torch.LongTensor)    # shape (200,) LongTensor = 64-bit integer
        self.dataset = {'x':x, 'y':y}

        self.net = Network(2,4,4,3)
        self.trainer = Trainer(self.net)

        self.trainer.x = self.dataset['x']
        self.trainer.y = self.dataset['y']

        self.assertTrue(self.trainer.accuracy ==  0.0)
        self.trainer.train(1000)
        self.assertTrue(self.trainer.accuracy >  0.9)


if __name__ == '__main__':
    unittest.main()