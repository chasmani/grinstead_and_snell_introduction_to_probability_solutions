import random

def take_a_shot():
	return random.randint(0,1)

def play_a_game():

	streak_count = 0

	total_shots = 20

	for i in range(total_shots):
		if take_a_shot():
			streak_count += 1
		else:
			streak_count = 0
		if streak_count == 5:
			return True

	return False

def simulate_games():

	runs = 1000

	win_count = 0
	for i in range(runs):
		if play_a_game():
			win_count += 1

	print("Over {} runs, had a streak {} times. Fraction of {}".format(runs, win_count, win_count/runs))

simulate_games()

