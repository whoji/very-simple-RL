import numpy as np
from game import Game
from agent import Agent

N = 1000000
IF_VERBO = True
MEMORY_LEN = 5

class RLController(object):

    def __init__(self):
        self.game = Game(memory_len = 5, money = 100)
        self.agent = Agent(memory_len = 5, money = 100)

        self.max_play_episodes = 10000

    def run(self, i=0):

        agent_action = self.agent.get_action()
        game_action = self.game.get_action()
        
        if IF_VERBO and i % round(N/100) == 0:
            print("Game %d : [%d vs %d]" % (i, agent_action, game_action))

        self.game.saw_action(agent_action)
        self.agent.saw_action(self.game.queue_enemy, self.game.queue_self)

        self.agent.meditate()

    def start_everything(self):
        for i in range(N):
            self.run(i)

            if i % round(N/100) == 0:
                pass
                # print winrate in last 100 game


if __name__ == '__main__':
    controller = RLController()
    controller.start_everything()