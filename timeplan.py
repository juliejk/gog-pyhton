def tull(x):
	time = open(x,'r')
	timer = []
	for line in time:
		y = line.split(',')
		y[-1] = y[-1].strip('\n')
		timer.append(y)
	time.close()
	return timer
	
def tull3(x,fn):
	sk = open(fn,'w')
	for i in x:
		sk.write(','.join(i)+'\n')
	sk.close()

def tull2(x,dag,time,fag):
	x[dag][time-8] = fag
	
mintime = tull('timeplan.csv')
tull2(mintime,0,10,'bla')
tull3(mintime,'julie.csv')

print "0) Avslutt\n1) AApne timeplan fra fil\n2) Lagre timeplan til fil\n3) Vis timeplan\n4) Legg til time til timeplan\n5) Fjern time fra timeplan\n6) Endre tidspunkt for time i timeplan"
sup = input('-')

if sup == 0:
	exit()
elif sup == 1:
	pass
	sup = 7
elif sup == 2:
	tull3(mintime,'julie.csv')
	sup = 7
elif sup == 3:
	print mintime
	sup = 7
elif sup == 4:
	dag1 = input('Hvilken dag onsker du aa endre paa: ')
	time1 = input('Hilken time onsker du aa endre paa: ')
	legg = raw_input('Legg til onsket fag: ')
	tull2(mintime,dag1,time1,str(legg))
	print mintime
	sup = 7
elif sup == 5:
	dag2 = input('Hvilken dag onsker du aa endre paa: ')
	time2 = input('Hilken time onsker du aa endre paa: ')
	tull2(mintime,dag2,time2,'')
	sup = 7
elif sup == 6:
	pass
	sup = 7
if sup == 7:
	print "0) Avslutt\n1) AApne timeplan fra fil\n2) Lagre timeplan til fil\n3) Vis timeplan\n4) Legg til time til timeplan\n5) Fjern time fra timeplan\n6) Endre tidspunkt for time i timeplan"
	sup = input('-')