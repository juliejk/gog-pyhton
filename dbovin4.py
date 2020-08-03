gbin = lambda x: x >= 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

def format(num, length):
	for i in range(0, length):
		if len(num) == length - i:
			return i*'0' + num
	return num

def hash(num, mod):
	return gbin(num%mod)

numbers = [2369, 3760, 4692, 4871, 5659, 1821, 1074, 7115, 1620, 2428, 3943, 4750, 6975, 4981, 9208]
strr=''

for num in numbers:
	num = str(num)
	strr+= 'Part#: ' + num + ' -> h(K) = ' + num + ' mod 128 -> ' + ' Hash: ' + format(str(hash(int(num), 128)), 7) + '\n'

f = open('file.txt', 'w')

f.write(strr)

print strr