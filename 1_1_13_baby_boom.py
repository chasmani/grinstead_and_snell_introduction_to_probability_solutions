import random

def proportion_of_boys_today(total_babies):

	boys = 0
	for i in range(total_babies):
		if random.randint(1,2) == 1:
			boys += 1
	return boys/total_babies


def simulate_hospitals():

	days = 365
	small_hospital_babies = 15
	large_hospital_babies = 45

	small_hospital_more_than_60_percent = 0
	large_hospital_more_than_60_percent = 0

	for i in range(days):
		if proportion_of_boys_today(15)>0.6:
			small_hospital_more_than_60_percent += 1

		if proportion_of_boys_today(45)>0.6:
			large_hospital_more_than_60_percent += 1

	print("Over {} days:".format(days))
	print("Hospital with 15 babies a day had {} days of more than 60% boys".format(small_hospital_more_than_60_percent))
	print("Hospital with 45 babies a day had {} days of more than 60% boys".format(large_hospital_more_than_60_percent))

simulate_hospitals()