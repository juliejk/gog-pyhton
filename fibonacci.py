x0 = 0
x1 = 1
tekst = str(x0) + ", " + str(x1)
for x in range(20):
    x2 = x0 + x1
    tekst += ", " + str(x2)
    x0 = x1
    x1 = x2
print tekst