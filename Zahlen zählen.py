#1

zahl = 1

while zahl <= 10:
    print(zahl)
    zahl += 1
#---------------------------------------

#2
summe = 0

eingabe = input("Bitte geben Sie eine Zahl ein (0 zum Beenden): ")
while eingabe != "0": # ! Ungleich 0
    try:
        zahl = float(eingabe)
        summe += zahl
    except ValueError:
        print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
    eingabe = input("Bitte geben Sie eine Zahl ein (0 zum Beenden): ")
print(f"Die Summe aller eingegebenen Zahlen ist: {summe}")
#------------------------------------------

#3
richtiges_passwort = "geheim123"
while True:
    eingabe = input("Bitte geben Sie das Passwort ein: ")

    if eingabe == richtiges_passwort:
        print("Zugang gewährt!")
        break
    else:
        print("Falsches Passwort! Versuchen Sie es erneut.")
#-----------------------------------------

#4
for zahl in range(1, 11): #range is only between numbers
    print(zahl)

#-------------------------------------------
#5

for i in range(1,21,2):
    i = i + 1
    print(i)
#5
for zahl in range(1,21,2):
    print(zahl)
zahlen = [4, 6, 8, 10, 12, 14, 16, 18, 20]
for i in range(0, len(zahlen), 5):
    print(zahlen[i])
#---------------------------------------------

#6
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
#-----------------------------------------------
#7
for zahl in range(10, 0, -1):
    print(zahl)
#----------------------------------------------
#8
namen = ["Anna", "Max", "Tom", "Lisa"]
namen.append("Marie")
print("Aktuelle Liste:", namen)
namen.remove("Tom")
print("Aktuelle Liste:", namen)
print("Länge der Liste:", len(namen))
#-----------------------------------------------
#9
zahlen = [5, 3, 8, 1, 2]

zahlen.sort()
print("Aufsteigend sortiert:", zahlen)
zahlen.sort(reverse=True)
print("Absteigend sortiert:", zahlen)
zahlen.reverse()
print("Reihenfolge umgekehrt:", zahlen)
#-----------------------------------------

#10
zahlen = [1, 2, 3, 4, 5]
zahlen.append(6)
zahlen.insert(0, 0)
anzahl_drei = zahlen.count(3)
print("Aktuelle Liste:", zahlen)
print("Anzahl der Zahl 3:", anzahl_drei)
#-----------------------------------------------
#11
werte = [10, 20, 30, 40, 50]
for wert in werte:
    print(wert)
#oder
werte = [10, 20, 30, 40, 50]
for index, wert in enumerate(werte):
    print(f"Wert an Position {index}: {wert}")
#-----------------------------------------------------
#12
zahlen = [10, 20, 30, 40, 50]
summe = sum(zahlen)
print("Summe der Elemente:", summe)
#-----------------------------------------------------
#13
text = "Programmieren"
for buchstabe in text:
    print(buchstabe)
#-----------------------------------------------------
#14
zahlen = [4, 11, 7, 15, 3, 22, 9, 18]
gefilterte_zahlen = [zahl for zahl in zahlen if zahl > 10]
print("Zahlen größer als 10:", gefilterte_zahlen)
#-----------------------------------------------------
#15
zahlen = [10, 20, 30, 40, 50]
for index, wert in enumerate(zahlen):
    print(f"Index: {index}, Wert: {wert}")
#------------------------------------------------------
#16
werte = [10, 20, 30, 40, 50]
for index, wert in enumerate(werte):
    print(f"Wert an Position {index}: {wert}")
#------------------------------------------------------