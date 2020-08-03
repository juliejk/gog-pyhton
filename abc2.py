import math

def d(a,b,c):
    d = (b**2-4*a*c)
    if d < 0: 
        svar = "to imagineare losninger"
    elif d == 0:
        svar = "en reell losning"
    else:
        svar = "to reelle losninger"    
    return str(a) + "x^2 + " +str(b) + "x + " + str(c) + " = 0 har " + str(svar)
    
a = input ("Skriv en verdi for a: ")
b = input ("Skriv en verdi for b: ")
c = input ("Skriv en verdi for c: ")
print d(a,b,c)