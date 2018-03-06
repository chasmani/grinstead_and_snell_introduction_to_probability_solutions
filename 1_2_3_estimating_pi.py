import random
import math

# Imageine a square of size 1,1.
# We will run a montecarlo simulation to randomly find points within this square
# Imagine a circle of radius 1/2, center 1/2,1/2. The probability of ladning in the circle is equal to area of circle, Pi/4
# By running a Monte Carlo simulation, and counting number of times we land in the circle, we can estimate Pi


def random_point():

	i = random.random()
	j = random.random()

	return i,j

def is_point_in_circle(point):

	distance_from_center = math.sqrt(math.pow(point[0]-0.5,2) + math.pow(point[1]-0.5,2))
	if distance_from_center<=0.5:
		return True
	else:
		return False


def run_simulation():

	runs = 1000000

	in_circle_count = 0
	for i in range(runs):
		if is_point_in_circle(random_point()):
			in_circle_count += 1

	print("In circle {} times in {} runs".format(in_circle_count, runs))
	print("Pi estimated to be {}".format(4*in_circle_count/runs))



run_simulation()