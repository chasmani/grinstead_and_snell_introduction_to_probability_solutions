
import random

def roll_dice():
	return random.randint(1,6)

def sum_of_3_dice():
	return roll_dice() + roll_dice() + roll_dice()

def count_results_frequency_9_10(runs):

	nine_count = 0
	ten_count = 0

	for i in range(runs):
		result = sum_of_3_dice()
		if result == 9:
			nine_count += 1
		elif result == 10:
			ten_count +=1

	print("Over {} runs. {} nines and {} tens".format(runs, nine_count, ten_count))

count_results_frequency_9_10(100000)


def calculate_number_of_ways_to_get_sum(target):

	ways = 0

	for dice_1 in range(1,7):
		for dice_2 in range(1,7):
			for dice_3 in range(1,7):
				total = dice_1 + dice_2 + dice_3
				if total == target:
					#print("{}, {}, {}".format(dice_1, dice_2, dice_3))
					ways += 1
	print("{} ways for {}".format(ways, target))

	print("Expected frequency is {}".format(ways/216))

calculate_number_of_ways_to_get_sum(9)
calculate_number_of_ways_to_get_sum(10)