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

        self.trainer.train(100)



    # def test_generate_action(self):
    #     # testing getting action from the game
    #     a = self.game.get_action()
    #     self.assertEqual(a, -1)
    #     self.assertEqual(self.game.queue_self, [0,1,-1,1,1,-1][1:]+[a])

    #     a = self.game.get_action()
    #     self.assertEqual(a, 0)
    #     self.assertEqual(self.game.queue_self, [0,1,-1,1,1,-1][2:]+[-1,0])

    # def test_intake_action(self):
    #     # testing game seeing an action (agent's action)
    #     a = 0
    #     self.game.saw_action(a)
    #     self.assertEqual(self.game.queue_enemy,  [0,0,-1,0,0,-1][1:] + [a])
    #     reward = Game.get_reward(-1, a)
    #     self.assertEqual(self.game.money_self, 100+reward)

    #     a = 0
    #     self.game.saw_action(a)
    #     self.assertEqual(self.game.queue_enemy,  [0,0,-1,0,0,-1][2:] + [0,0])
    #     reward_2 = Game.get_reward(-1, a)
    #     self.assertEqual(self.game.money_self, 100+reward+reward_2)
    #     self.assertEqual(self.game.money_enemy, 100-reward-reward_2)


if __name__ == '__main__':
    unittest.main()