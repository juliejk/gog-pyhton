a = input ("Skriv en verdi for a: ")
b = input ("Skriv en verdi for b: ")
c = input ("Skriv en verdi for c: ")

d =(b**2-4*a*c)
if d<0:
    print "Svaret er imagineart"

elif d==0:
    print "Svaret har kun en losning"

elif d>0:
    print "Svaret har to losninger"