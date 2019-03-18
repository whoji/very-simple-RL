import numpy as np
import unittest
from game import Game

class TestGame(unittest.TestCase):
    """docstring for ClassName"""
    def setUp(self):
        self.game = Game()
        print(self.game.queue_self)
        print(self.game.queue_enemy)
        print("Resetting game queue")
        self.game.queue_self = [0,1,-1,1,1,-1]
        self.game.queue_enemy = [0,0,-1,0,0,-1]
        print(self.game.queue_self)
        print(self.game.queue_enemy)
        print("")

    def test_generate_action(self):
        # testing getting action from the game
        a = self.game.get_action()
        self.assertEqual(a, -1)
        self.assertEqual(self.game.queue_self, [0,1,-1,1,1,-1][1:]+[a])

        a = self.game.get_action()
        self.assertEqual(a, 0)
        self.assertEqual(self.game.queue_self, [0,1,-1,1,1,-1][2:]+[-1,0])

    def test_intake_action(self):
        # testing game seeing an action (agent's action)
        a = 0
        self.game.saw_action(a)
        self.assertEqual(self.game.queue_enemy,  [0,0,-1,0,0,-1][1:] + [a])
        reward = Game.get_reward(-1, a)
        self.assertEqual(self.game.money_self, 100+reward)

        a = 0
        self.game.saw_action(a)
        self.assertEqual(self.game.queue_enemy,  [0,0,-1,0,0,-1][2:] + [0,0])
        reward_2 = Game.get_reward(-1, a)
        self.assertEqual(self.game.money_self, 100+reward+reward_2)
        self.assertEqual(self.game.money_enemy, 100-reward-reward_2)


if __name__ == '__main__':
    unittest.main()