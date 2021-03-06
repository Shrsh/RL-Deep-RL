import gym
from gym import Wrapper
from gym.wrappers import Monitor
from gym import error, version, logger
import os, json, numpy as np, six
from gym.wrappers.monitoring import stats_recorder, video_recorder
from gym.utils import atomic_write, closer
from gym.utils.json_utils import json_encode_np
import numpy as np
import sys
import random
import numpy as np
import os
import matplotlib.pyplot as plt

class Control:

	#global declarations 
	#==================
	# --HYPERPARAMETERS--
	total_episodes = 50000      	# Total episodes
	learning_rate = 0.8 		    # Learning rate
	max_steps = 2000				# Max steps per episode
	gamma = 0.99	 	            # Discount Factor
	epsilon = 0.9                   # minimum epsilon for epsilon greedy policies
	env =  ""
	monitor_path = ""				# path for recording monitor videos
	record = False					#boolean variable for recording the videos using monitor



	def __init__(self,total_episodes,learning_rate,max_steps,gamma,env,epsilon,path):

		self.monitor_path = os.path.join(path, "monitor")
		self.total_episodes = total_episodes
		self.learning_rate  = learning_rate
		self.max_steps 		= max_steps
		self.gamma 			= gamma
		self.epsilon        = epsilon

		if not os.path.exists(self.monitor_path):
			os.makedirs(self.monitor_path)
		self.env = gym.make(env)

		
	def greedy_policy_action(self,q_table,state,i_episode):
		eps = 0.9
		decay = 0.9999
		for i in range(i_episode):
			eps= max(self.epsilon, eps*decay)
		random_number = random.uniform(0,1)
		if random_number < eps:
			return self.env.action_space.sample() 
		else:
			return np.argmax(q_table[state],axis=0)

	def results(self,q_table,rewards):
		print(q_table)
		plt.plot(rewards)
		plt.show()
		self.env.render()

	def Q_Learning(self):
		

	def SARSA(self):
		"""
		SARSA using epsilon greedy policy.  
		env: OpenAI Gym Environment 
		"""
		# q- value table 
		state_size = self.env.observation_space.n
		action_space_size = self.env.action_space.n
		q_table = np.zeros([state_size, action_space_size])
		count_table = np.zeros([state_size, action_space_size])
		total_reward = []

		# Record videos
		self.env= Monitor(self.env,
				 directory=self.monitor_path,
				 resume=True,
				 video_callable=self.record)

		for i_episode in range(self.total_episodes):
			reward_per_episode = 0
			state = self.env.reset()
			step = 0
			done = False
			if i_episode % 1000 == 0:
			   print("\rEpisode {}/{}.".format(i_episode, self.total_episodes))
			   sys.stdout.flush()
			   self.record = True
			else:
				self.record = False
			action = self.greedy_policy_action(q_table,state,i_episode)

			while done == False: 	
				new_state, reward, done, info = self.env.step(action) 
				reward_per_episode += reward
				next_action = self.greedy_policy_action(q_table,new_state,i_episode)
				q_table[state][action] += self.learning_rate*(reward + self.gamma*q_table[new_state][next_action] - q_table[state][action])
				state = new_state
				action = next_action
			total_reward.append(reward_per_episode)
		self.results(q_table,total_reward)


	def monte_carlo_on_policy_control(self):
		"""
		Monte Carlo Control using Epsilon-Greedy policies.
		env: OpenAI gym environment.
		"""

		# q- value table
		state_size = self.env.observation_space.n
		action_space_size = self.env.action_space.n
		q_table = np.zeros([state_size, action_space_size])
		count_table = np.zeros([state_size, action_space_size])

		for i_episode in range(self.total_episodes):
			state = self.env.reset()
			step = 0
			done = False
			if i_episode % 1000 == 0:
			   print("\rEpisode {}/{}.".format(i_episode, self.total_episodes))
			   sys.stdout.flush()

			#generate an episode 
			episode = []
			for steps in range(self.max_steps):
				if done:
					break
				#epsilon_greedy_policy
				action = self.greedy_policy_action(q_table,state,i_episode)
				new_state, reward, done, info = self.env.step(action)
				episode.append([state, action, reward])
				state = new_state

			#update the Q-values
			for i in range(state_size):
				for j in range(action_space_size):
					returns_ = 0 #total reward obtained after this state
					state_id = -1 #state id of the state being processed
					count = 0 #number of time the state 'i,j' is visited
					start_counting_reward = False #count rewards from this state
					#for each state, search the whole episode for the first occurence of that state and then calculate returns from there. 
					for k in range(len(episode)):
						if episode[k][0] == i  and episode[k][1] == j:
							count_table[i][j] +=1
							count+=1
							start_counting_reward = True
							if count == 1:
								state_id = k
						if start_counting_reward: 
							returns_ += np.power(self.gamma,k - state_id)*episode[k][2]
					if count> 0:
						q_table[i][j]+=(1/count_table[i][j])*(returns_ - q_table[i][j]) 
						
			del episode
		self.results(q_table)



path = ""
env = Control(100000,0.8,5000,0.99,"Taxi-v2",0.1,path)
# train_monte_carlo(env, value_table)
env.SARSA()




