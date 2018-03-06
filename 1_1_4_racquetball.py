import random


def play_point(serve):
	

	if serve == True:
		win_probability = 0.6
	else:
		win_probability = 0.5
	
	if random.randint(1,10) <= (win_probability*10):
		return True
	else:
		return False

def test_play_point_function(runs):

	win_times = 0
	for i in range(runs):
		if play_point(True):
			win_times+=1
	print("Expected win times {}, actual win times {}".format(0.6*runs, win_times))

	win_times = 0
	for i in range(runs):
		if play_point(False):
			win_times+=1
	print("Expected win times {}, actual win times {}".format(0.5*runs, win_times))

def play_game():

	my_points = 0
	opponent_points = 0

	my_serve = True

	while (my_points<21 and opponent_points<21):
		point_result = play_point(my_serve)
		my_serve = point_result

		if point_result:
			my_points += 1
		else:
			opponent_points += 1

	#print("Me: {}, Opponent: {}".format(my_points, opponent_points))

	if my_points> opponent_points:
		return True
	else:
		return False

def simulate_games(runs):

	win_count = 0

	for i in range(runs):
		if play_game():
			win_count += 1

	print("Won {} times out of {} games".format(win_count, runs))
	print("This suggests a win probability of {}".format(win_count/runs))

simulate_games(10000)





