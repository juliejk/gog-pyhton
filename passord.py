x,y = raw_input("passord: "),raw_input("passord igjen: ")
z = x.strip('0123456789')
w = x.strip('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
if x != y or len(x) < 7 or x.isalpha() or x.isdigit() or z.isupper() or z.islower() or len(w) == len(x):
    print "Feil ass"
else:
    print "Nailed it"