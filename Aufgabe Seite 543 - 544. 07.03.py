# Aufgabe 2
nummer = 3  # Integer (Ganzzahl)
name = "Müller, Karl"  # String (Text)
alter = 34  # Integer (Ganzzahl)
adresse = "Mühlenweg 1A, 01069 Dresden"  # String (Text)
telefonnummer = "0177-1234567"  # String (Text, da Telefonnummern oft Sonderzeichen enthalten)
beruf = "Fachinformatiker"  # String (Text)
verheiratet = True  # Boolean (True/False)
lohnsteuerkasse = #integer  # Boolean (True/False)
anzahl_kinder = 2  # Integer (Ganzzahl)
lohn_gehalt = 2870.00  # Float (Gleitkommazahl)

# Ausgabe der Variablen zur Überprüfung
print("Laufende Nummer:", nummer)
print("Name des Mitarbeiters:", name)
print("Alter des Mitarbeiters:", alter)
print("Adresse:", adresse)
print("Telefonnummer:", telefonnummer)
print("Beruf:", beruf)
print("Verheiratet:", verheiratet)
print("Lohnsteuerkasse:", lohnsteuerkasse)
print("Anzahl der Kinder:", anzahl_kinder)
print("Lohn/Gehalt:", lohn_gehalt)
############

# Aufgabe 3
print("123 % 7 =", 123 % 7)
print("12345 % 100 =", 12345 % 100)
print("121 % 11 =", 121 % 11)
print("8 % 2 =", 8 % 2)
print("9 % 2 =", 9 % 2)
print("3 % 5 =", 3 % 5)

# Aufgabe 4
x = 12

x += 12
#12 + 12 = 24
print("Nach + x = 12:", x)
x = 12
x -= 12
#12-12 = 0
print("Nach x -= 12:", x)
x = 12
x *= 12
#12*12=144
print("Nach x *= 12:", x)
x = 12
x /= 12
#12/12=1.0
print("Nach x /= 12:", x)
x = 12
x %= 12
#12%12= 0
print("Nach x %= 12:", x)
##############

# Aufgabe 5
kilometer = float(input("Gib die gefahrenen Kilometer ein: "))
kraftstoffmenge = float(input("Gib die getankte Kraftstoffmenge in Litern ein: "))
durchschnittsverbrauch = (kraftstoffmenge / kilometer) * 100
print(f"Der Durchschnittsverbrauch beträgt: {durchschnittsverbrauch:.2f} Liter pro 100 km.")

# Aufgabe 6
spannung = float(input("Gib die elektrische Spannung in Volt ein: "))
stromstaerke = float(input("Gib die elektrische Stromstärke in Ampere ein: "))
widerstand = spannung / stromstaerke
print(f"Der elektrische Widerstand beträgt: {widerstand:.2f} Ohm.")

# Aufgabe 7
hoehe = int(input("Gib die Höhe des Bildes in Pixeln ein: "))
breite = int(input("Gib die Breite des Bildes in Pixeln ein: "))
speicher_pro_pixel = int(input("Gib den Speicherbedarf pro Pixel in Byte ein: "))
anzahl_bilder = int(input("Gib die Anzahl der Bilder ein: "))
speicher_byte = hoehe * breite * speicher_pro_pixel * anzahl_bilder
speicher_gib = speicher_byte / (1024 ** 3)
print(f"Der Speicherplatzbedarf beträgt: {speicher_gib:.2f} GiB.")