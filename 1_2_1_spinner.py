import random

import numpy as np
import matplotlib.pyplot as plt


def spin():
	return random.random()


def run_experiment():

	runs = 10000

	semicircle_landed = 0
	third_circle_landed = 0
	sextant_landed = 0

	for i in range(runs):
		result = spin()

		if 0 <= result < 0.5:
			semicircle_landed += 1
		elif 0.5 <= result < 0.66666666666:
			sextant_landed += 1
		else:
			third_circle_landed += 1

	print("Results after {} runs".format(runs))
	print("Semicircle: {}".format(semicircle_landed))
	print("Sextant: {}".format(sextant_landed))
	print("Third of a circle: {}".format(third_circle_landed))

	semicircle_center = 0.25
	semicircle_width = 0.5
	semicircle_height = semicircle_landed/semicircle_width

	sextant_center = (0.5 + 1/12)
	sextant_width = (1/6)
	sextant_height = sextant_landed/sextant_width

	third_center = 1- (1/6)
	third_width = 1/3
	third_height = third_circle_landed/third_width

	plt.bar([semicircle_center, sextant_center, third_center], [semicircle_height, sextant_height, third_height], [semicircle_width, sextant_width, third_width], color=["r","g", "b"])
	plt.show()



#plt.bar(x values, heights, width)


run_experiment()

