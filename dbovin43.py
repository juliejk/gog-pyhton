numbers = [2369, 3760, 4692, 4871, 5659, 1821, 1074, 7115, 1620, 2428, 3943, 4750, 6975, 4981, 9208]
svar = ''

for num in numbers:
    num = int(num)
    num = num % 128
    svar += (str(num) + ', ')
    
print svar