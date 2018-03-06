import random

import numpy as np

def time_until_next_occurence():
	
	if random.random() <0.1:
		return 73
	else:
		return 3

def run_experiment_once():

	observation_start = 100
	end_condition = False
	time = 0
	
	while end_condition == False:
		
		# Time only recorded at t = 0 and when there is an occurence
		time += time_until_next_occurence()

		if (time > 100):
			return time - 100


def run_simulation():

	number_of_experiments = 1000

	results = []
	for i in range(number_of_experiments):
		results.append(run_experiment_once())

	print("Mean waiting time over {} runs is {}".format(number_of_experiments, np.mean(results)))


run_simulation()