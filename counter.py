from collections import Counter

rader = open('exercise2.txt').readlines ()
print 'Fila har  %i rader' % (len(rader) )

def tull(x):
	fil = open(x)
	tegn = fil.read().split(' ')
	cn = Counter(tegn).most_common(10)
	return cn
	
y = tull('exercise2.txt')
for i in range(1,len(y)):
	print "%s: %i" % (y[i][0].strip('.0000000e+00').strip('.0000000e+00\n'), y[i][1])
