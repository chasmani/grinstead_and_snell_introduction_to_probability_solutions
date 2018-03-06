import random

def toss_coins(n):

	heads = 0
	count = 0
	for i in range(n):
		count += 1
		if random.randint(1,2) == 1:
			heads += 1


	heads_proportion = heads/count
	if 0.4 < heads_proportion < 0.6:
		return True
	else:
		return False
	

def run_experiment(n):

	within_range_count = 0

	runs = 100

	for i in range(runs):
		if toss_coins(n):
			within_range_count += 1
	print("For n of {}, heads proportion was within range {} out of {} runs".format(n, within_range_count, runs))

run_experiment(100)

