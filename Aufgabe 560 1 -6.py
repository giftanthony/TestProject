#2
anzahl = 6
i = 0
summe = 0
temperaturen = []  # Anlegen einer leeren Liste

while i < anzahl:
    print("Geben Sie die {0}. Temperatur in °C ein:".format(i+1))
    eingabe = float(input())
    temperaturen.append(eingabe)  # Eingabe zur Liste hinzufügen
    summe = summe + eingabe
    i += 1

durchschnitt = summe / anzahl

print("\nDie eingegebenen Temperaturen sind:")
for temp in temperaturen:
    print(temp)

print("\nDie Durchschnittstemperatur beträgt:", durchschnitt, "°C")

#------------------------------------------

#3
import random  # Modul für Zufallszahlen einbinden

anzahl = 10  # Erhöhte Anzahl der Temperaturen (z. B. 10)
summe = 0
temperaturen = []  # Leere Liste für die Temperaturen

# Schleife zur Generierung und Speicherung der Zufallstemperaturen
for i in range(anzahl):
    zufallstemperatur = random.uniform(-10.0, 35.0)  # Zufallszahl zwischen -10°C und 35°C
    temperaturen.append(zufallstemperatur)  # Temperatur zur Liste hinzufügen
    summe += zufallstemperatur  # Temperatur zur Summe addieren
    print(f"Temperatur {i+1}: {zufallstemperatur:.1f}°C")  # Ausgabe der generierten Temperatur

durchschnitt = summe / anzahl  # Berechnung des Durchschnitts
print(f"\nDurchschnittstemperatur: {durchschnitt:.1f}°C")  # Ausgabe des Durchschnitts

#------------------------------------
#4
for zahl in range(1,12):
    print(zahl)
#------------------------------------
#5
# Liste der gewünschten Sternanzahlen für jede Zeile
stern_anzahlen = [7, 5, 3, 1]

# Schleife über jede Zeile
for anzahl in stern_anzahlen:
    # Schleife für die Ausgabe der Sterne in einer Zeile
    for i in range(anzahl):
        print('*', end='')  # Ein Stern pro Durchlauf, kein Zeilenumbruch
    print()  # Zeilenumbruch nach jeder Sternreihe

# Ausgabe des Pluszeichens in der letzten Zeile
print('+')
#---------------------------------------------
#6
# Eingabe der ganzen Zahl vom Benutzer
zahl = int(input("Geben Sie eine ganze Zahl ein: "))

# Initialisierung der Fakultät mit 1 (da 0! = 1 und 1! = 1)
fakultaet = 1

# Berechnung der Fakultät mit einer Schleife
if zahl < 0:
    print("Fehler: Fakultät ist für negative Zahlen nicht definiert!")
else:
    for i in range(1, zahl + 1):
        fakultaet *= i  # Multiplikation der Werte von 1 bis zahl

    # Ausgabe des Ergebnisses
    print(f"Die Fakultät von {zahl} ist {fakultaet}.")