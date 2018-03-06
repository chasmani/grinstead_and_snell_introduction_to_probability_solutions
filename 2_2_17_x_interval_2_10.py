import random


def random_x():

	return (random.random() * 8 ) + 2 


def simulate():

	runs = 1000

	count_x_greater_5 = 0
	count_x_between_5_7 = 0
	count_quadratic = 0

	for run in range(runs):

		number = random_x()

		if number > 5:
			count_x_greater_5 += 1

		if 5 < number < 7:
			count_x_between_5_7 += 1

		if (number**2 - (12*number) +35) >0:
			count_quadratic += 1

	print("Over {} runs:".format(runs))
	print("Fraction x > 5: \t {}".format(count_x_greater_5/runs))
	print("Fraction 5 < x < 7: \t {}".format(count_x_between_5_7/runs))
	print("Fraction x^2 -12x +35 > 0: \t {}".format(count_quadratic/runs))


simulate()