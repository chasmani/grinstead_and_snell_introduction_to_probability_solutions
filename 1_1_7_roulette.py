import random

def spin_roulette_number(number):
	result = random.randint(0,37)
	if result == number:
		return True
	else:
		return False

def spin_roulette_black_red():
	result = random.randint(0,37)
	if result == 0:
		return False
	if result%2 == 0:
		return True


def test_roulette():

	runs = 10000

	win_count = 0
	for i in range(runs):
		if spin_roulette_black_red():
			win_count += 1
	win_numbers = 18
	expected_win_percentage = win_numbers/38

	print("Over {} runs expected {} wins. Got {} wins".format(runs, expected_win_percentage*runs, win_count))

	win_count = 0
	for i in range(runs):
		if spin_roulette_number(17):
			win_count += 1
	win_numbers = 1
	expected_win_percentage = win_numbers/38

	print("Over {} runs expected {} wins. Got {} wins".format(runs, expected_win_percentage*runs, win_count))


def simulate_winnings_red():

	money = 0
	for i in range(500):
		if spin_roulette_black_red():
			money += 1
		else:
			money -= 1

	print("Winnings after 500 bets on red: {}".format(money))

def simulate_winnings_17():

	money = 0
	for i in range(500):
		if spin_roulette_number(17):
			money += 35
		else:
			money -= 1

	print("Winnings after 500 bets on 17: {}".format(money))




simulate_winnings_17()
