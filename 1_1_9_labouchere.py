import random

def spin_roulette_black_red():
	result = random.randint(0,37)
	if result == 0:
		return False
	if result%2 == 0:
		return True

def get_bet_amount(lab_list):
	if len(lab_list)==1:
		return lab_list[0]
	else:
		return lab_list[0] + lab_list[-1]

def play_game():

	lab_list = [1,2,3,4]
	money = 0

	while len(lab_list) >0:

		bet_amount = get_bet_amount(lab_list)

		if spin_roulette_black_red():
			money += bet_amount
			lab_list = lab_list[1:-1]
		else:
			money -= bet_amount
			lab_list.append(bet_amount)

		print("Current balance: {}. Current list: {}".format(money, lab_list))

	print(money)

play_game()