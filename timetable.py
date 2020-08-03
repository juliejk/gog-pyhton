from csv import reader,

def schedule(fileReader):
        temp = [[None]*8 for i in range(5)]
        for j,row in enumerate(fileReader):
                for i in range(0,len(row)):
                        if row[i]:
                                temp[j][i] = row[i]
                        else:
                                pass
        return temp
 
def add_top_table(tableIn, top):
        for i in range(0,len(top)):
                tableIn[0][i] = top[i]
        return tableIn
 
def add_first_collum(tableIn, firstCollum):
        for i in range(0,len(firstCollum)):
                tableIn[i+1][0] = firstCollum[i]
        return tableIn
 
def timetable(schedule, days, times):
        temp = [[None]*6 for i in range(9)]
        temp = add_top_table(temp, days)
        temp = add_first_collum(temp, times)
        for j,row in enumerate(schedule):
                for i in range(len(row)):
                        if temp[i+1][j+1] == None:
                                temp[i+1][j+1] = row[i]
        return temp
 
def print_timetable(timetable):
        for j,row in enumerate(timetable):
                for i in range(len(row)):
                        if timetable[j][i] != None:
                                print "%s\t" % timetable[j][i],
                        else:
                                print "\t",
                print "\n",
        print "\n"
 
def write_timetable_to_file(timetable, filename, timetableForTime):
        fileWriter = writer(open(filename + '.csv', 'wb'), delimiter=',', quotechar='"')
        for row in timetable:
                fileWriter.writerow(row)
        timesWriter = writer(open('timetableTo' + fileName + '.csv', 'wb'), delimiter=',', quotechar='"')
        timesWriter.writerow(timetableForTime)
 
def change_times(tableIn, collum, change):
        tableIn[collum] = change
        return tableIn
 
def change_class(tableIn, row, collum, change):
        tableIn[row][collum] = change
        return tableIn
 
def open_timetable(filename):
        csvOut = reader(open(filename + '.csv', 'rb'), delimiter=',', quotechar='"')
        return csvOut
 
fileReader = reader(open('timeplan.csv', 'rb'), delimiter=',', quotechar='"')
days =['Tid', 'Man', 'Tirs', 'Ons', 'Tors', 'Fre']
times =['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00']
personTimeTable = schedule(fileReader)
notFinished = True
valg = ''
 
while notFinished:
        print 'Velkommen! Du vil faa noen valg'
        print '0) Avslutt\n1) Aapne timeplan fra fil\n2) Lagre timeplan til fil\n3) Vis timeplan\n4) Legg time til timeplan\n5) Fjern time fra timeplan\n6) Endre tidspunkt for time i timeplan\n'
        valg = raw_input('> ')
 
        if valg == '0':
                notFinished = False
        elif valg == '1':
                fileName = raw_input('Skriv inn filnavn (uten filtype)\n> ')
                fileReader = open_timetable(fileName)
        elif valg == '2':
                outputFileName = raw_input('Skriv hva filnavnet skal hete (uten filtype)\n> ')
                write_timetable_to_file(personTimeTable, outputFileName, times)
        elif valg == '3':
                print_timetable(timetable(personTimeTable, days, times))
        elif valg == '4':
                row = input('Skriv inn tallet paa raden du vil endre\n> ')
                collum = input('Skriv inn tallet paa kolonnen du vil endre\n> ')
                changeTo = raw_input('Hva vil du endre det til?\n> ')
                personTimeTable = change_class(personTimeTable, row, collum, changeTo)
        elif valg == '5':
                row = input('Skriv inn tallet paa raden du vil fjerne\n> ')
                collum = input('Skriv inn tallet paa kolonnen du vil fjerne\n> ')
                personTimeTable = change_class(personTimeTable, row, collum, None)
        elif valg == '6':
                collum = input('Skriv inn tallet paa tiden du vil endre paa\n> ')
                changeTo = raw_input('Skriv inn hva du vil endre det til (XX:XX)\n> ')
                times = change_times(times, collum, changeTo)
        else:
                print 'Du skreiv noe feil'