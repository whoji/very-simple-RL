import numpy as np
from game import Game
from agent import Agent

N = 1000000
IF_VERBO = True
MEMORY_LEN = 6
EPSILON = 0.7
EPSILON_DECAY = 0.99999
TEMPO_WINDOW = 1000
LEARNING_RATE = 0.02

class RLController(object):

    def __init__(self):
        self.game = Game(memory_len = 5, money = 100)
        self.agent = Agent(memory_len = 5, money = 100, 
            eps = EPSILON, eps_decay = EPSILON_DECAY, lr = LEARNING_RATE)

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
            print("Average (reward, winrate) in last %d games: (%.3f, %.3f)" 
                % (TEMPO_WINDOW, round(sum(self.agent_rewards)/TEMPO_WINDOW,3),  
                    round(sum([r for r in self.agent_rewards if r > 0])/TEMPO_WINDOW,3)))
            self.agent_rewards = []

    def start_everything(self):
        for i in range(N):
            self.run(i)


if __name__ == '__main__':
    controller = RLController()
    controller.start_everything()