import random
nummer = random.randint(0,1000)
tall = input("Gjett et tall mellom 0 og 1000: ")
antall = 1

while (tall != nummer) and (antall <= 10):

	sum = 10 - antall
	if tall > nummer:
		print "For hoyt"
		print "Du har", sum, "forsok igjen"
		tall = input("Gjett et nytt tall mellom 0 og 1000: ")
		antall += 1
	 
	elif tall < nummer:
		print "For lavt"
		print "Du har", sum, "forsok igjen"
		tall = input("Gjett et nytt tall mellom 0 og 1000: ")
		antall += 1
	
	elif tall == nummer:
		print "Congratz! Du klarte det! Tallet var ", nummer
		yn = raw_input("Vil du starte paa nytt spill? y/n" )
		if yn == 'n':
			break
		elif yn == 'y':
			nummer = random.randint(0,1000)
			tall = raw.input("Gjett et tall mellom 0 og 1000: ")
			antall = 1


	if (antall > 10):
		print "Game Over, you were eaten by a Grue"