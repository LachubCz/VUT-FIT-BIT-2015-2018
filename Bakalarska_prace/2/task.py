"""
docstring
"""
import sys
import gym
from gym import wrappers
from agent import Agent
from playing import Playing as pl
from visualization import point_graph, gaussian_graph, combined_graph

class Task:
    """
    docstring
    """
    def __init__(self, args):
        self.args = args
        self.name = None
        self.env = None
        self.env_state_size = None
        self.env_action_size = None
        self.type = None
        self.solved_score = None
        self.average_rand_score = None
        self.max_steps = None
        self.agent = None
        self.test = None
        self.envs = {"CartPole-v0" : self.cartp0,
                     "CartPole-v1" : self.cartp1,
                     "MountainCar-v0" : self.mcar0,
                     "Acrobot-v1" : self.acro1,
                     "Pong-v0" : self.pong1,
                     "Breakout-v0" : self.break0,
                    }
        self.envs[args.environment]()

    def cartp0(self):
        """
        docstring
        """
        self.name = self.args.environment
        self.env = gym.make(self.name)
        self.env_state_size = self.env.observation_space.shape[0]
        self.env_action_size = self.env.action_space.n
        self.type = "vect"
        self.solved_score = 195
        self.average_rand_score = 22.25
        self.max_steps = 200
        self.agent = Agent(self.args.algorithm, self.env_state_size, self.env_action_size,
                           self.args.network, self.args.memory)
        self.test = self.cartp0_test

    def cartp0_test(self, scores, episodes_numbers):
        """
        docstring
        """
        complete_estimation = pl.score_estimate_vect(self, 10)
        if complete_estimation >= self.solved_score:
            for i in range(2, 11):
                estimation = pl.score_estimate_vect(self, 10)
                complete_estimation = complete_estimation + estimation
                if (complete_estimation / i) < self.solved_score:
                    return
        else:
            return
        score = complete_estimation / 10

        if score > self.solved_score:
            self.agent.save_model_weights("{}-solved.h5" .format(self.name))
            print("Task solved after {} episodes with score {}." .format(episodes_numbers[-1], score))
            point_graph(scores, episodes_numbers, "{}-point_graph.png" .format(self.name))
            gaussian_graph(scores, episodes_numbers, "{}-gaussian_graph.png" .format(self.name))
            combined_graph(scores, episodes_numbers, "{}-combined_graph.png" .format(self.name))
            sys.exit()

    def cartp1(self):
        """
        docstring
        """
        self.name = self.args.environment
        self.env = gym.make(self.name)
        self.env_state_size = self.env.observation_space.shape[0]
        self.env_action_size = self.env.action_space.n
        self.type = "vect"
        self.solved_score = 475
        self.average_rand_score = 22.25
        self.max_steps = 500
        self.agent = Agent(self.args.algorithm, self.env_state_size, self.env_action_size,
                           self.args.network, self.args.memory)
        self.test = self.cartp1_test

    def cartp1_test(self, scores, episodes_numbers):
        """
        docstring
        """
        complete_estimation = pl.score_estimate_vect(self, 10)
        if complete_estimation >= self.solved_score:
            for i in range(2, 11):
                estimation = pl.score_estimate_vect(self, 10)
                complete_estimation = complete_estimation + estimation
                if (complete_estimation / i) < self.solved_score:
                    return
        else:
            return
        score = complete_estimation / 10

        if score > self.solved_score:
            self.agent.save_model_weights("{}-solved.h5" .format(self.name))
            print("Task solved after {} episodes with score {}." .format(episodes_numbers[-1], score))
            point_graph(scores, episodes_numbers, "{}-point_graph.png" .format(self.name))
            gaussian_graph(scores, episodes_numbers, "{}-gaussian_graph.png" .format(self.name))
            combined_graph(scores, episodes_numbers, "{}-combined_graph.png" .format(self.name))
            sys.exit()

    def mcar0(self):
        """
        docstring
        """
        self.name = self.args.environment
        self.env = gym.make(self.name)
        self.env_state_size = self.env.observation_space.shape[0]
        self.env_action_size = self.env.action_space.n
        self.type = "vect"
        self.solved_score = -110
        self.average_rand_score = -200
        self.max_steps = 200
        self.agent = Agent(self.args.algorithm, self.env_state_size, self.env_action_size,
                           self.args.network, self.args.memory)
        self.test = self.mcar0_test

    def mcar0_test(self, scores, episodes_numbers):
        """
        docstring
        """
        complete_estimation = pl.score_estimate_vect(self, 10)
        if complete_estimation >= self.solved_score:
            for i in range(2, 11):
                estimation = pl.score_estimate_vect(self, 10)
                complete_estimation = complete_estimation + estimation
                if (complete_estimation / i) < self.solved_score:
                    return
        else:
            return
        score = complete_estimation / 10

        if score > self.solved_score:
            self.agent.save_model_weights("{}-solved.h5" .format(self.name))
            print("Task solved after {} episodes with score {}." .format(episodes_numbers[-1], score))
            point_graph(scores, episodes_numbers, "{}-point_graph.png" .format(self.name))
            gaussian_graph(scores, episodes_numbers, "{}-gaussian_graph.png" .format(self.name))
            combined_graph(scores, episodes_numbers, "{}-combined_graph.png" .format(self.name))
            sys.exit()

    def acro1(self):
        """
        docstring
        """
        self.name = self.args.environment
        self.env = gym.make(self.name)
        self.env_state_size = self.env.observation_space.shape[0]
        self.env_action_size = self.env.action_space.n
        self.type = "vect"
        self.solved_score = -100
        self.average_rand_score = -498.95
        self.max_steps = 500
        self.agent = Agent(self.args.algorithm, self.env_state_size, self.env_action_size,
                           self.args.network, self.args.memory)
        self.test = self.acro1_test

    def acro1_test(self, scores, episodes_numbers):
        """
        docstring
        """
        """
        complete_estimation = pl.score_estimate_vect(self, 10)
        if complete_estimation >= self.solved_score:
            for i in range(2, 11):
                estimation = pl.score_estimate_vect(self, 10)
                complete_estimation = complete_estimation + estimation
                if (complete_estimation / i) < self.solved_score:
                    return
        else:
            return
        score = complete_estimation / 10

        if score > self.solved_score:
            self.agent.save_model_weights("{}-solved.h5" .format(self.name))
            print("Task solved after {} episodes with score {}." .format(episodes_numbers[-1], score))
            point_graph(scores, episodes_numbers, "{}-point_graph.png" .format(self.name))
            gaussian_graph(scores, episodes_numbers, "{}-gaussian_graph.png" .format(self.name))
            combined_graph(scores, episodes_numbers, "{}-combined_graph.png" .format(self.name))
            sys.exit()
        """
        if episodes_numbers[-1] == 100:
            score = pl.score_estimate_vect(self, 100)
            self.agent.save_model_weights("{}-solved.h5" .format(self.name))
            print("Task solved after {} episodes with score {}." .format(episodes_numbers[-1], score))
            point_graph(scores, episodes_numbers, "{}-point_graph.png" .format(self.name))
            gaussian_graph(scores, episodes_numbers, "{}-gaussian_graph.png" .format(self.name))
            combined_graph(scores, episodes_numbers, "{}-combined_graph.png" .format(self.name))
            sys.exit()

    def pong1(self):
        """
        docstring
        """
        self.name = self.args.environment
        self.env = gym.make(self.name)
        self.env_state_size = (2, 84, 84)
        self.env_action_size = self.env.action_space.n
        self.type = "img"
        self.solved_score = float("-inf")
        self.average_rand_score = float("-inf")
        self.max_steps = 10000
        self.agent = Agent(self.args.algorithm, self.env_state_size, self.env_action_size,
                           self.args.network, self.args.memory)
        self.test = self.acro1_test

    def pong1_test(self, scores, episodes_numbers):
        """
        docstring
        """
        pass


    def break0(self):
        """
        docstring
        """
        self.name = self.args.environment
        self.env = gym.make(self.name)
        self.env_state_size = (2, 84, 84)
        self.env_action_size = self.env.action_space.n
        self.type = "img"
        self.solved_score = float("-inf")
        self.average_rand_score = float("-inf")
        self.max_steps = 10000
        self.agent = Agent(self.args.algorithm, self.env_state_size, self.env_action_size,
                           "basic_img", self.args.memory)
        self.test = self.acro1_test

    def break0_test(self, scores, episodes_numbers):
        """
        docstring
        """
        pass