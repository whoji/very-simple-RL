import numpy as np
from game import Game
from agent import Agent

N = 100000
IF_VERBO = True

class RLController(object):

    def __init__(self):
        self.env = Game(memory_len = 5, money = 100)
        self.agent = Agent()

        self.max_play_episodes = 10000

    def run(self):

        agent_action = agent.get_action()
        game_action = agent.get_action()
        
        if IF_VERBO:
            print("%d vs %d" % (agent_action, game_action))

        agent.saw_action(agent_action)
        agent.saw_action(env.queue_enemy, env.queue_self)

        agent.meditate()

    def start_everything(self):
        for i in range(N):
            self.run()

            if i % 100 == 0:
                pass
                # print winrate in last 100 game


if __name__ == '__main__':
    controller = RLController()
    controller.start_everything()