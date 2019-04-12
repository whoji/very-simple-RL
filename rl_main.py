import numpy as np
from game import Game
from agent import Agent

N = 1000000
IF_VERBO = True
MEMORY_LEN = 5
EPSILON = 0.3
EPSILON_DECAY = 0.9999
TEMPO_WINDOW = 1000

class RLController(object):

    def __init__(self):
        self.game = Game(memory_len = 5, money = 100)
        self.agent = Agent(memory_len = 5, money = 100, 
            eps = EPSILON, eps_decay = EPSILON_DECAY)

        self.max_play_episodes = 10000
        self.agent_rewards = []

    def run(self, i=0):

        agent_action = self.agent.get_action()
        game_action = self.game.get_action()
        
        if IF_VERBO and i % round(N/TEMPO_WINDOW) == 0:
            print("Game %d/%d : [%d vs %d]" % (i, N, agent_action, game_action), end=" | ")

        self.game.saw_action(agent_action)
        self.agent.saw_action(self.game.queue_enemy, self.game.queue_self)

        self.agent.meditate()

        self.agent_rewards.append(Agent.get_reward(agent_action,game_action))
        if len(self.agent_rewards) == TEMPO_WINDOW:
            print("Average reward in last %d games: %.3f" % (TEMPO_WINDOW, 
                round(sum(self.agent_rewards)/TEMPO_WINDOW,3)))
            self.agent_rewards = []

    def start_everything(self):
        for i in range(N):
            self.run(i)

            if i % round(N/100) == 0:
                pass
                # print winrate in last 100 game


if __name__ == '__main__':
    controller = RLController()
    controller.start_everything()