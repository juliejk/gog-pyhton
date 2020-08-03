X = input ("Skriv inn en x-verdi: ")
OP = raw_input("Skriv inn en operator: ")
Y = input ("Skriv inn en y-verdi: ")

if OP == "+":
 z=X+Y
 print z

elif OP == "-":
 z=X-Y
 print z

elif OP == "*":
 z=X*Y
 print z

elif OP == "/" and Y != 0 :
 z=X/Y
 print z

else:
 print "Feilaktig input"
 exit()
 
if z%2==0:
  print z, "er et partall"

else:
  print z, "er et oddetall"
  
if int (z) < z:
 print "Tallet har desimaler"

else:
 print "Tallet er et heltall"