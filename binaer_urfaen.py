from time import sleep
import datetime

now = datetime.datetime.now()
a, b, c = now.hour, now.minute, now.second

def ten_to_bi(tall):
	if tall == 0:
		sek1 = 0
		sek2 = 0
		sek3 = 0
	elif tall == 1:
		sek1 = 0
		sek2 = 0
		sek3 = 1
	elif tall == 2:
		sek1 = 0
		sek2 = 1
		sek3 = 0
	elif tall == 3:
		sek1 = 0
		sek2 = 1
		sek3 = 1
	elif tall == 4:
		sek1 = 1
		sek2 = 0
		sek3 = 0
	elif tall == 5:
		sek1 = 1
		sek2 = 0
		sek3 = 1
	elif tall == 6:
		sek1 = 1
		sek2 = 1
		sek3 = 0
	elif tall == 7:
		sek1 = 1
		sek2 = 1
		sek3 = 1
	return sek1, sek2, sek3


def binaer_ur(a, b, c):
	sek_tall = c%8
	eight_tall = c//8
	min_tall = b%8
	eight_min = b//8
	hour_sek = a%8
	hour_min = a//8
	while True:
		sek1, sek2, sek3 = ten_to_bi(sek_tall)
		eight_sek1, eight_sek2, eight_sek3, = ten_to_bi(eight_tall)
		min_tall1, min_tall2, min_tall3, = ten_to_bi(min_tall)
		eight_min1, eight_min2, eight_min3, = ten_to_bi(eight_min)
		hour_sek1, hour_sek2, hour_sek3 = ten_to_bi(hour_sek)
		hour_min1, hour_min2, hour_min3 = ten_to_bi(hour_min)
		print("",hour_min1, hour_sek1, eight_min1, min_tall1, eight_sek1, sek1, "\n",hour_min2, hour_sek2, eight_min2, min_tall2, eight_sek2, sek2, "\n",hour_min3, hour_sek3, eight_min3, min_tall3, eight_sek3, sek3, "\n")
		sleep(1)
		sek_tall += 1
		if eight_tall == 7 and sek_tall == 4:
			sek_tall = 0
			eight_tall = 0
			min_tall += 1
		if min_tall == 8:
			min_tall = 0
			eight_min += 1
		if sek_tall == 8:
			sek_tall = 0
			eight_tall += 1
		if eight_min == 7 and min_tall == 4:
			min_tall = 0
			eight_min = 0
			hour_sek += 1
		if hour_sek == 8:
			hour_sek = 0
			hour_min += 1
		if hour_min == 3:
			hour_min = 0
			

binaer_ur(a, b, c)