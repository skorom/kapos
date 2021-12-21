import string
#import MySQLdb

file=open("Angol.txt", "r", encoding="utf-8")
#szavak beolvasása
szavak=[]
for i in file:
    szavak.append(i.strip("\n").lower())
abc=string.ascii_lowercase

#szavak betűkké változtatása
szavak2=[]

for szo in szavak:
    temp=""
    for i in range(len(abc)):
        if(abc[i] in szo):
            temp+=abc[i]
    szavak2.append(temp)
file.close()

#szavak értékekké változtatása betűik gyakoriság alapján
gyakor=open("betugyakorisag", "r", encoding="utf-8")
ertekek=[]
gyakorisag=[]
#gyakorisag beolvasása
for i in gyakor:
    gyakorisag.append(float(i.strip("\n")))
#lista feltolese 0-kal
for i in range(len(szavak)):
    ertekek.append(0)

#szavak ertekenek kiszamolasa
i=0
for string in szavak2:
    for j in range(len(string)):
        ertekek[i] +=  0.125 - gyakorisag[abc.find(string[j])]
    ertekek[i]=round(ertekek[i], 3)
    i+=1

#besorolas

mydb = MySQLdb.connect(
    host="localhost",
    user="root",
    password="",
    database="dusza"
)

j=0
for szam in ertekek:
    mycursor = mydb.cursor()
    if (szam < 0.3):
        mycursor.execute(
            "INSERT INTO konnyu_angol (szo) VALUES('" + szavak[j] + "')")
        mydb.commit()
    elif szam >= 0.3 and szam < 0.5:
        mycursor.execute(
            "INSERT INTO kozepes_angol (szo) VALUES('" + szavak[j] + "')")
        mydb.commit()
    elif szam >= 0.5:
        mycursor.execute(
            "INSERT INTO nehez_angol (szo) VALUES('" + szavak[j] + "')")
        mydb.commit()
    j += 1

print(szavak)
print(szavak2)
