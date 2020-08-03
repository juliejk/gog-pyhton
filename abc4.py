a = input ("Skriv en verdi for a: ")
if a == 0:
    print "Du kan ikke bruke abc-formelen uten et x^2 ledd. DUST!"
else:
    b = input ("Skriv en verdi for b: ")
    c = input ("Skriv en verdi for c: ")
    d =(b**2-4*a*c)

    def bla(x,y,w):
        z = ""
        if x > 0 and y != 0:
            z = "+"
        if x == 1 and y != 2:
            x = ""
        elif x == -1 and y != 2:
            x = "-"
        elif x == 0:
            x = ""
            w = ""
        return z + str(x) + w
    
    if d < 0: 
        print bla(a,0,"x^2 ") + bla(b,1,"x ") + bla(c,2,"") + " = 0 har to imagineare losninger"
    elif d == 0:
        print bla(a,0,"x^2 ") + bla(b,1,"x ") + bla(c,2,"") + " = 0 har en reell losning"
    else:
        print bla(a,0,"x^2 ") + bla(b,1,"x ") + bla(c,2,"") + " = 0 har to reelle losninger"