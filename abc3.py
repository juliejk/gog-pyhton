tall = []
for i in range(3):
    tall.append(input("Skriv et tall: "))

if tall[0] == 0:
    print "Du kan ikke bruke abc-formelen uten et x^2 ledd. DUST!"
else:
    d =(tall[1]**2-4*tall[0]*tall[2])
    if d < 0: 
        svar = "to imagineare losninger"
    elif d == 0:
        svar = "en reell losning"
    else:
        svar = "to reelle losninger"

    for i in range(3):
        y = ""
        if tall[i] > 0 and i != 0:
            y = "+"
        if i != 2:
            if tall[i] == 1:
                tall[i] = ""
            elif tall[i] == -1:
                tall[i] = "-"        
        tall.append(str(y + str(tall[i])))

    output = tall[3] + "x^2"
    if tall[1] != 0:
        output += tall[4] + "x"
    if tall[2] != 0:
        output += tall[5]
    print output + "=0 har " + svar