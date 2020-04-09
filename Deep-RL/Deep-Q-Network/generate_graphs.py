import matplotlib.pyplot as plt 
import numpy 
import os


file  = open("rewards_file.txt", "r")
list_ = file.readlines()
reward_array = []
for i in range(len(list_)):
    reward_array.append(float((list_[i].strip('\n'))))
file.close()
x = [30*i for i in range(len(reward_array))]
plt.plot(x, reward_array)
plt.show()
