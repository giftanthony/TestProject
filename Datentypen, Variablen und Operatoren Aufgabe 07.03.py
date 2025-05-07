# Aufgabe 1:
integer = 100
float = 12.34
string = "Hallo Python!"
boolean = True
print("Integer-Wert:", integer)
print("Float-Wert:", float)
print("String:", string)
print("Boolescher Wert:", boolean)
###############

# Aufgabe 2:
integer = 100
float = 12.34
string = "Hallo Python!"
boolean = True

print("Typ von integer:", type(integer))
print("Typ von float:", type(float))
print("Typ von string:", type(string))
print("Typ von boolean:", type(boolean))

integer = "Ich bin jetzt ein String"
float = False
string = 123
boolean = 3.14

print("\nNach der Änderung:")
print("Typ von integer:", type(integer))
print("Typ von float:", type(float))
print("Typ von string:", type(string))
print("Typ von boolean:", type(boolean))
################

# Aufgabe 3 Fstrigs
name = input("Gib deinen Namen ein: ")
zahl = float(input("Gib eine Zahl ein: "))
ergebnis = zahl * 10
print(f"Hallo {name}, das Ergebnis ist: {ergebnis}")
#################

# Aufgabe 4
addition = 15 + 7
print("15 + 7 =", addition)
subtraktion = 100 - 45
print("100 - 45 =", subtraktion)
multiplikation = 8 * 6
print("8 * 6 =", multiplikation)
division = 81 / 9
print("81 / 9 =", division)
modulo = 10 % 3
print("10 % 3 =", modulo)
potenz = 2 ** 5
print("2 ** 5 =", potenz)
ganzzahlige_division = 23 // 5
print("23 // 5 =", ganzzahlige_division)
###############

# Aufgabe 5
temperatur1 = float(input("Gib die erste Temperatur ein: "))
temperatur2 = float(input("Gib die zweite Temperatur ein: "))
temperatur3 = float(input("Gib die dritte Temperatur ein: "))
durchschnitt = (temperatur1 + temperatur2 + temperatur3) / 3
print("Die Durchschnittstemperatur beträgt:", durchschnitt)
####################

# Aufgabe 6
ganzzahl = int(input("Gib eine Ganzzahl ein: "))
kommazahl = float(ganzzahl)
print("kommazahl:", kommazahl)

zahl_als_string = input("Gib eine Zahl als String ein: ")
zahl_als_integer = int(zahl_als_string)
print("Zahl als Integer:", zahl_als_integer)

boolesche_variable = True
bool_als_integer = int(boolesche_variable)
print("Boolesche Variable als Integer:", bool_als_integer)