import random

def roll_dice():
	return random.randint(1,6)

def sum_of_3_dice():
	return roll_dice() + roll_dice() + roll_dice()

def run_game(rolls):

	for i in range(rolls):
		if sum_of_3_dice() == 18:
			return True
	return False

def simulate(rolls):

	simulation_runs = 1000

	win_count = 0

	for i in range(simulation_runs):
		if run_game(rolls):
			win_count += 1

	win_fraction = win_count/simulation_runs
	print("For {} rolls, win count over {} runs was {}. Or as a fraction {}".format(rolls, simulation_runs, win_count, win_fraction))

	
	if win_fraction < 0.55:
		simulate(rolls + 1)
	

simulate(145)

