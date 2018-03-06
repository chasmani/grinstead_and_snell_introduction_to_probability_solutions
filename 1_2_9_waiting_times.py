import random
import math

import matplotlib.pyplot as plt
import numpy as np


average_time = 30

def waiting_time():

	return - average_time * math.log(random.random())

def simulate():

	data = []
	runs = 10000

	for i in range(runs):
		data.append(waiting_time())

	
	plt.hist(data, bins=24, range=(0,120))
	
	t = np.arange(0., 120., 1)

	lines = plt.plot(t, runs*5*(1/30)*np.exp(-(1/30)*t), 'r--')
	
	plt.show()


simulate()