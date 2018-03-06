import random
import math


length = 1

def random_point_and_angle():

	i = random.random() * length/2
	j = random.random() * length/2
	theta = random.random() * (math.pi/2)

	return i,j,theta

def does_needle_cross_a_line(point):

	d1_test = (length/2) * math.sin(point[2])
	if point[0] <= d1_test:
		return True

	d2_test = (length/2) * math.cos(point[2])
	if point[1] <= d2_test:
		return True

	return False


def run_simulation():

	runs = 10000

	in_area_count = 0
	for i in range(runs):
		if does_needle_cross_a_line(random_point_and_angle()):
			in_area_count += 1

	print("In area {} times in {} runs".format(in_area_count, runs))

	in_area_proportion = in_area_count/runs

	pi_estimate = (4*length - (length*length))/in_area_proportion


	print("Pi estimated to be {}".format(pi_estimate))


run_simulation()