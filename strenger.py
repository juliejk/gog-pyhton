def like(ord1,ord2):
    if len(ord1) == len(ord2):
        for i in range(len(ord1)):
            if ord1[i] != ord2[i]:
                return False
            else:
                continue
        return True
    else:
        return False

def rever(ord):
    return ord[::-1]
    
def palin(ord):
    if rever(ord) == ord:
        return True
    else:
        False
       
def inni(ord1,ord2):
    for i in range(len(ord1)):
        if ord1[i:i+len(ord2)] == ord2:
            return i
        else: 
            continue
    return False  

ord1 = raw_input("Skriv et ord: ")
ord2 = raw_input("Skriv enda et ord: ")
if like(ord1,ord2) == True:
    print ord1, "og", ord2, "er like"
else:
    print ord1, "og", ord2, "er ikke like"

if inni(ord1,ord2) != False:
    print ord1, "inneholder", ord2, " fra og med", inni(ord1,ord2)
    
ord3 = raw_input("Skriv et ord du vil reversere: ")
print ord3, "reversert er", rever(ord3)
if palin(ord3) == True:
    print ord3, "er et palindrom"
else:
    print ord3, "er ikke et palindrom"