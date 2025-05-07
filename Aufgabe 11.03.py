#Aufgabe 1
zahl = float(input("Geben Sie eine Zahl ein: "))
if zahl > 0:
    print("Die Zahl ist positiv.")
####################

#Aufgabe 2
zahl = int(input("Geben Sie eine ganze Zahl ein: "))
if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
####################

#Aufgabe 3
alter = int(input("Wie alt bist du? "))
if alter >= 18:
    print("Du bist volljährig.")
else:
    print("Du bist noch nicht volljährig.")
######################

#Aufgab 4
punktzahl = int(input("Gib deine Punktzahl ein (0-100): "))
if punktzahl >= 90 and punktzahl <= 100:
    print("Sehr gut")
elif punktzahl >= 80 and punktzahl <= 89:
    print("Gut")
elif punktzahl >= 70 and punktzahl <= 79:
    print("Befriedigend")
elif punktzahl >= 60 and punktzahl <= 69:
    print("Ausreichend")
elif punktzahl < 60 and punktzahl >= 0:
    print("Nicht bestanden")
else:
    print("Fehler: Die Punktzahl muss zwischen 0 und 100 liegen!")
###########################

#Aufgabe 5
temperatur = float(input("Gib die Temperatur in Grad Celsius ein: "))
if temperatur > 30:
    print("Es ist heiß!")
elif temperatur >= 20 and temperatur <= 30:
    print("Das Wetter ist angenehm.")
else:
    print("Es ist kalt!")
###########################

#Aufgabe 6
name = input ("Wie heiß du? ")
print(f"Hallo {name}! Schön, dich zu sehen!")

def begrüße():
    name = input ("Wie heiß du? ")
    print(f"Hallo {name}! Schön, dich zu sehen!")
begrüße()
############################

#Aufgabe 7
def addiere(a, b):
    return a + b
ergebnis = addiere(4, 6)
print("Die Summe ist:", ergebnis)
###########################

#Aufgabe 8
def max_wert(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("Der größte Wert ist:", max_wert(10, 20, 15))
###########################

#Aufgabe 9
def prüfe_zahl(n):
    if n > 0:
        print("Die Zahl ist positiv.")
    elif n < 0:
        print("Die Zahl ist negativ.")
    else:
        print("Die Zahl ist null.")
zahl = float(input("Gib eine Zahl ein: "))
prüfe_zahl(zahl)
###########################

#Aufgabe 10
def quadratischer_wert(n):
    return n ** 2

def hauptfunktion():
    zahl = float(input("Gib eine Zahl ein: "))
    ergebnis = quadratischer_wert(zahl)
    print(f"Das Quadrat von {zahl} ist: {ergebnis: .2f}")
hauptfunktion()
#############################

#Aufgabe 11
def benutzer_menü():
    while True:
        print("\nWähle eine Rechenoperation:")
        print("1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Division")
        print("5. Beenden")

        auswahl = input("Gib die Nummer der gewünschten Operation ein (1-5): ")

        if auswahl == "5":
            print("Programm beendet.")
            break

        if auswahl not in ["1", "2", "3", "4"]:
            print("Ungültige Auswahl! Bitte wähle eine Zahl zwischen 1 und 5.")
            continue

        zahl1 = float(input("Gib die erste Zahl ein: "))
        zahl2 = float(input("Gib die zweite Zahl ein: "))

        if auswahl == "1":
            ergebnis = zahl1 + zahl2
            print(f"Das Ergebnis der Addition ist: {ergebnis}")
        elif auswahl == "2":
            ergebnis = zahl1 - zahl2
            print(f"Das Ergebnis der Subtraktion ist: {ergebnis}")
        elif auswahl == "3":
            ergebnis = zahl1 * zahl2
            print(f"Das Ergebnis der Multiplikation ist: {ergebnis}")
        elif auswahl == "4":
            if zahl2 == 0:
                print("Fehler: Division durch Null ist nicht erlaubt!")
            else:
                ergebnis = zahl1 / zahl2
                print(f"Das Ergebnis der Division ist: {ergebnis}")
benutzer_menü()
