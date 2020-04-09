import gym
from gym import Wrapper
from gym import error, version, logger
import os, json, numpy as np, six
from gym.wrappers.monitoring import stats_recorder, video_recorder
from gym.utils import atomic_write, closer
from gym.utils.json_utils import json_encode_np
import numpy as np
import sys


#global declarations 
#==================
# --HYPERPARAMETERS--
global total_episodes
total_episodes = 20000      	# Total episodes
global learning_rate 
learning_rate = 0.8 		    # Learning rate
global max_steps 
max_steps = 20000				# Max steps per episode
global gamma 
gamma = 0.99	 	            # Discount Factor


def train_monte_carlo(env, value_table):
	'''
	Function for monte carlo policy evaluation 
	Args: 
	    * env - gym enviroment object 
	    * value_table - Value function table

	'''
	for i in range(total_episodes):
		state = env.reset()
		step = 0
		done = False
		# if i % 1000 == 0:
  #       	print("\rEpisode {}/{}.".format(i, total_episodes))
  #           sys.stdout.flush()

		#generate an episode 
		episode = []
		for steps in range(max_steps):
			if done:
				break
			#random policy
			action = env.action_space.sample() 
			new_state, reward, done, info = env.step(action)
			episode.append([state, action, reward])
			state = new_state
		

		#update the values
		for i in range(state_size):
			returns_ = 0 #total reward obtained after this state
			state_id = -1 #state id of the state being processed
			count = 0 #number of time the state 'i' is visited
			start_counting_reward = False #count rewards from this state
			#for each state, search the whole episode for the first occurence of that state 
			for j in range(len(episode)):
				if episode[j][0] == i:
					count+=1
					start_counting_reward = True
					returns_ += episode[j][2]
					state_id = j
				if start_counting_reward: 
					returns_ += np.power(gamma,j - state_id)*episode[j][2]
			if count> 0:
				value_table[i]+=(1/count)*(returns_/count - value_table[i]) 
	

env = gym.make("FrozenLake8x8-v0")
#value table
state_size = env.observation_space.n
action_space_size = env.action_space.n
# print(state_size)
# print(env.observation_space)
value_table = np.zeros(state_size)
q_table = np.zeros([state_size, action_space_size])

# train_monte_carlo(env, value_table)
monte_carlo_epsilon_greedy(env, q_table)

print(value_table)
env.render()



	

