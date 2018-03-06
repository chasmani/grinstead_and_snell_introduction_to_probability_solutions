import random
import math


def random_point():

	i = random.random()
	j = random.random()

	return i,j

def is_point_in_area(point):

	max_y = math.sin(math.pi * point[0])

	if point[1] < max_y:
		return True
	else:
		return False


def run_simulation():

	runs = 1000000

	in_area_count = 0
	for i in range(runs):
		if is_point_in_area(random_point()):
			in_area_count += 1

	print("In area {} times in {} runs".format(in_area_count, runs))
	print("Area estimated to be {}".format(in_area_count/runs))

	print("Pi estimated to be {}".format(2/(in_area_count/runs)))



run_simulation()