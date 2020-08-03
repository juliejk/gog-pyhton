import datetime
x = raw_input("YYYY.MM.DD.:")


dat = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lordag", "Sondag"]
mat = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]

aar = x[0] + x[1] + x[2] + x[3]
maaned = x[5] + x[6]
dag = x[8] + x[9]

dt = datetime.date(int(aar),int(maaned), int(dag))

print dat[dt.weekday()], int(dag), mat[maaned*10], int(arr)

