# Aufgabe 2: # int oder float works!
#The "def" keyword is used correctly to define a function.
# This function is named beispiel_aufgabe, and it performs
# the task of calculating and printing the average. (It calculate numbers only)
def kleinste_zahl():
    zahl1 = int(input("Geben Sie die erste Zahl ein: "))
    zahl2 = int(input("Geben Sie die zweite Zahl ein: "))
    if zahl1 < zahl2:
        print(f"Die kleinste Zahl ist: {zahl1}")
    else:
        print(f"Die kleinste Zahl ist: {zahl2}")

kleinste_zahl()
#Placing the call kleinste_zahl() at the end simply executes
# everything defined inside the function

zahl1 = int(input("Geben Sie die erste Zahl ein: "))
zahl2 = int(input("Geben Sie die zweite Zahl ein: "))
if zahl1 < zahl2:
        print(f"Die kleinste Zahl ist: {zahl1}")
else:
        print(f"Die kleinste Zahl ist: {zahl2}")
####################

#Aufgabe 3 int oder float
def groesste_zahl():
    zahl1 = int(input("Geben Sie die erste Zahl ein: "))
    zahl2 = int(input("Geben Sie die zweite Zahl ein: "))
    zahl3 = int(input("Geben Sie die dritte Zahl ein: "))
    groesste = max(zahl1, zahl2, zahl3)
    print(f"Die größte Zahl ist: {groesste}")

groesste_zahl()
######################

#Aufgabe 4
def gerade_oder_ungerade():
    zahl = int(input("Geben Sie eine ganze Zahl ein: "))
    if zahl % 2 == 0:
        print(f"Die Zahl {zahl} ist gerade.")
    else:
        print(f"Die Zahl {zahl} ist ungerade.")

gerade_oder_ungerade()
######################

#Aufgabe 5
#The "def" keyword is used correctly to define a function.
# This function is named beispiel_aufgabe, and it performs
# the task of calculating and printing the average. (It calculate numbers only)
def schaltjahr_pruefen():
    jahr = int(input("Geben Sie eine Jahreszahl ein: "))
    if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
        print(f"Das Jahr {jahr} ist ein Schaltjahr.")
    else:
        print(f"Das Jahr {jahr} ist kein Schaltjahr.")

schaltjahr_pruefen()
#Placing the call beispiel_aufgabe() at the end simply executes
# everything defined inside the function

jahr = int(input("Geben Sie eine Jahreszahl ein: "))
if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
        print(f"Das Jahr {jahr} ist ein Schaltjahr.")
else:
        print(f"Das Jahr {jahr} ist kein Schaltjahr.")
#####################

#Aufgabe 6
#The "def" keyword is used correctly to define a function.
# This function is named beispiel_aufgabe, and it performs
# the task of calculating and printing the average. (It calculate numbers only)
def beispiel_aufgabe():
    zahl1 = float(input("Geben Sie die erste Zahl ein: "))
    zahl2 = float(input("Geben Sie die zweite Zahl ein: "))
    zahl3 = float(input("Geben Sie die dritte Zahl ein: "))
    durchschnitt = (zahl1 + zahl2 + zahl3) / 3
    print(f"Der Durchschnitt der Zahlen ist: {durchschnitt:.2f}")
    #print("Der Durchschnitt der Zahlen ist: {:.2f}".format(durchschnitt))
    #print("Der Durchschnitt der Zahlen ist: %.2f" % durchschnitt)

beispiel_aufgabe()
#Placing the call beispiel_aufgabe() at the end simply executes
# everything defined inside the function

zahl1 = float(input("Geben Sie die erste Zahl ein: "))
zahl2 = float(input("Geben Sie die zweite Zahl ein: "))
zahl3 = float(input("Geben Sie die dritte Zahl ein: "))
durchschnitt = (zahl1 + zahl2 + zahl3) / 3
print(f"Der Durchschnitt der Zahlen ist: {durchschnitt:.2f}")