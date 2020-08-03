import datetime
ukedager = ['Mandag','Tirsdag','Onsdag','Torsdag','Fredag','Lordag','Sondag']
maned = ['Januar','Februar','Mars','April','Mai','Juni','Juli','August','September','Oktober','November','Desember']
inputDato = raw_input('Skriv inn dato pa formen YYYY.MM.DD: ')
dt = datetime.date(int(inputDato[0:4]),int(inputDato[5:7]),int(inputDato[8:10]))
print ukedager[dt.weekday()], inputDato[8:10]+".",maned[int(inputDato[5:7])-1], int(inputDato[0:4])

inputDatoTekst = raw_input("Skriv inn dato som <ukedag> DD. <maned> YYYY: ")

inputUkedag = inputDatoTekst[0:inputDatoTekst.find(' ')].title()
inputManed = inputDatoTekst[inputDatoTekst.find('. ')+2:inputDatoTekst.rfind(' ')].title()
if not (inputUkedag in ukedager):
print "Ugyldig ukedag"
elif not (inputManed in maned):
print "Ugyldig maned"
else:
inputAr = inputDatoTekst[inputDatoTekst.rfind(' ')+1:len(inputDatoTekst)]
inputDagNr = inputDatoTekst[inputDatoTekst.find(' ')+1:inputDatoTekst.find('. ')]
newdt = datetime.date(int(inputAr),int(maned.index(inputManed)+1),int(inputDagNr))
if (inputUkedag.title() != ukedager[newdt.weekday()]):
print "Feil ukedag"
else:
print "Gyldig dato"

# Oppg C
inputDatoC = raw_input('Skriv inn dato som YYYY.MM.DD: ')
dtC = datetime.date(int(inputDatoC[0:4]),int(inputDatoC[5:7]),int(inputDatoC[8:10]))
dtJul = datetime.date(int(inputDatoC[0:4]), 12, 24)
JulDelta = dtJul - dtC
DagerTilJul = JulDelta.days
if DagerTilJul < 0:
print "Det er", DagerTilJul*-1, "dager siden jul"
elif DagerTilJul == 0:
print "Det er julaften i dag"
else:
print "Det er", DagerTilJul, "dager til jul"

# Oppg D
inputDatoD = raw_input('Skriv inn dato som YYYY.MM.DD: ')
JulDato = int(inputDatoD[8:10])
JulManed = int(inputDatoD[5:7])
if JulDato > 24 and JulManed == 12:
forrigeAr = int(inputDatoD[0:4])
nesteAr = int(inputDatoD[0:4])+1
else:
forrigeAr = int(inputDatoD[0:4])-1
nesteAr = int(inputDatoD[0:4])

dtD = datetime.date(int(inputDatoD[0:4]),JulManed,JulDato)

dtJul = datetime.date(nesteAr, 12, 24)
dtJulForrige = datetime.date(forrigeAr, 12, 24)
JulDelta = dtJul - dtD
ForrigeJulDelta = dtD - dtJulForrige
DagerTilJul = JulDelta.days
DagerTilForrigeJul = ForrigeJulDelta.days
print "Forrige jul er", DagerTilForrigeJul, "dager siden"
print "Neste jul er om", DagerTilJul, "dager"
if DagerTilJul > DagerTilForrigeJul:
print "Kortest til forrige jul"
else:
print "Kortest til neste jul"