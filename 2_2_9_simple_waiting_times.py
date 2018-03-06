import random
import math

import numpy as np

# We are given the density function. Integrating that with limits of 1 and 0 gives us the probability of an event in the next 1 minute

def probability_in_next_minute(decay_constant):
	"""
	Integrated lamda*exp(-lamda * t) with limits of 1 and 0, in order to get this function
	"""
	return (1 - math.exp(-decay_constant))


def test_probability_function():
	decay_constant = 1
	# Exercise 2.2.5 in the textbook gives this result to be .632
	print("Expected probabiltiy of decay in next second is {}, functon returned {}".format(0.632, probability_in_next_minute(decay_constant)))


def is_occurence(decay_constant):
	# State space is 0 <= X <=1, with X being a random variable

	if random.random() < probability_in_next_minute(decay_constant):
		return True
	return False


def run_experiment_once():

	decay_constant = 0.1
	observation_start = 100
	end_condition = False
	run_count = 0
	wait_time = 0

	while end_condition == False:
		run_count += 1

		if is_occurence(decay_constant) and (run_count > 100):
			end_condition = True

		if run_count > 100:
			wait_time += 1

	return wait_time


def run_simulation():

	number_of_experiments = 1000

	results = []
	for i in range(number_of_experiments):
		results.append(run_experiment_once())

	print("Mean waiting time over {} runs is {}".format(number_of_experiments, np.mean(results)))


run_simulation()