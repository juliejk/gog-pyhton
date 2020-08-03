import random

orm_x=[3,3,3,2,1] #slangens start x-posisjon
orm_y=[2,3,4,4,4] #slangens start y-posisjon

#a
def lag_tomt_brett(storrelse):
    brett= [[1]*storrelse for i in range(storrelse)] #lager brett med storrelse som lengde på x- og y-akse
    return brett
#b
def legg_ut_epler(storrelse, epler):
    brett=lag_tomt_brett(storrelse) #skriver inn brett uten noe
    for i in range (epler): #hvor mange epler du setter ut
        eple_x=random.randint(0,storrelse-1) #eplet sin x-posisjon
        eple_y=random.randint(0,storrelse-1) #eplet sin y-posisjon
        brett[eple_y][eple_x]=5 #legger eple som 5 tall på brett
    return brett
#c
def sjekk_eple(orm_x, orm_y, brett):
    hode_x=orm_x[0]
    hode_y=orm_y[0]
    if brett[hode_y][hode_x]==5: #sjekker om hodet spiser et eple
        return True
    else:
        return False
#d
def tegne_orm(orm_x, orm_y, brett):
    N = len(orm_x) # orm_x og orm_y skal være like lange
    for i in range(N): 
        x=orm_x[i]
        y=orm_y[i]
        if i == N-1: #tegne hale som 1 tall
            brett[y][x]=1
        else:
            brett[y][x]=0
        
    return brett

#e
def sjekk_krasj(orm_x, orm_y, retning):
    N = len(orm_x)
    hode_x = orm_x[0]
    hode_y = orm_y[0]
    if retning == 'n': #om retning er nord endres hodeposisjon en plass opp etc
        hode_y = hode_y-1
    elif retning == 'e':
        hode_x = hode_x+1
    elif retning == 's':
        hode_y = hode_y+1
    elif retning == 'w':
        hode_x = hode_x-1
    for i in range (N): 
        if hode_x==orm_x[i] and hode_y==orm_y[i]: #sjekker for alle i i lengden orm om nytt hodeposisjon treffer resten av kroppen
            return True
    return False

 #f
def flytt_orm(orm_x, orm_y, retning):
    N = len(orm_x) #lengde liste
    temp_x = orm_x[0]
    temp_y = orm_y[0]
    for i in range(N-1,0,-1): #fra bakerst av orm til 0 med endring -1 hver gang
        orm_x[i] = orm_x[i-1] #x og y-posisjon flyttes slik at siste posisjon blir den som før var nest sist etc
        orm_y[i] = orm_y[i-1]
    orm_x[0] = temp_x #midlertidig hode, men hodeposisjon fra før flyttet
    orm_y[0] = temp_y #samme...
    if retning == 'n':         # retning bestemmer hva ny x-eller y-posisjon skal være
        orm_y[0] = orm_y[0]-1
    elif retning == 'e':
        orm_x[0] = orm_x[0]+1
    elif retning == 's':
        orm_y[0] = orm_y[0]+1
    elif retning == 'w':
        orm_x[0] = orm_x[0]-1
    return orm_x,orm_y

#print hele brett før flytting
brett=legg_ut_epler(10, 10)
ut = tegne_orm(orm_x, orm_y, brett)
for i in range(len(ut)):
    print ut[i]

#sjekk om krasj med seg selv
retning='e' #for å endre retning endre mellom n, s, e, w
print sjekk_krasj(orm_x, orm_y, retning)

#flytting
orm_x, orm_y = flytt_orm(orm_x, orm_y, retning)

#print hele brett etter flytting
ut = tegne_orm(orm_x,orm_y, brett)
for i in range(len(ut)):
    print ut[i]