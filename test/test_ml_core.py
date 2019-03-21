import numpy as np
import unittest
import torch
from ml_core import Network, Trainer, ExpReplay

class TestMLCore(unittest.TestCase):
    """docstring for ClassName"""
    def setUp(self):
        self.net = Network(4,3,2,2)
        self.trainer = Trainer()

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
        self.net = Network(4,3,2,2)
        self.trainer.x = self.dataset['x']
        self.trainer.y = self.dataset['y']

        self.assertTrue(self.trainer.accuracy ==  0.0)
        self.trainer.train(100)
        self.assertTrue(self.trainer.accuracy >  0.9)


if __name__ == '__main__':
    unittest.main()