# Aufgabe 1
print("Hallo, Python-Welt!")
print("Ich lerne gerade Python.")
print("Programmieren macht Spaß!")
############

# Aufgabe 2 (Frage ohne Escape-Sequenz. Funktioniert auch nur mit Leerzeichen und
# man erhält das gleiche Ergebnis, oder?)
print("Name: Max Mustermann")
print("Beruf: \tSoftwareentwickler")
print("Wohnort: Hamburg")
################

# Aufgabe 3
name = input("Wie heißt du?? ")
compliment = input(f"Guten mogen {name} Es ist uns eine Freude, dich in unserem Unternehmen zu haben! ")
################

# Aufgabe 4 String umwandeln auf float!

zahl1 = input("How much do you have? : ")
zahl2 = input("How much do you want to give out? : ")
zahl3 = input("How much will be left if you give again 17€? : ")
zahl1 = float(zahl1)
zahl2 = float(zahl2)
zahl3 = float(zahl3)
summe = zahl1 - zahl2 - zahl3
print(summe)
###############

# Aufgabe 5 FString
artikel = input(input the product)
preis = int input(give the price"")
menge = 3
gesamtpreis = preis * menge
print(f"Artikel: {artikel}\nPreis: {preis:.2f} €\nMenge: {menge}\nGesamtpreis: {gesamtpreis:.2f} €")
# oder print(gesamtpreis) für nur der ergebnisse!
###############

# Aufgabe 6 Fstings
wechselkurs = 1.10
euro_betrag = float(input("Gib den Betrag in Euro ein: "))
dollar_betrag = euro_betrag * wechselkurs
print(f"{euro_betrag:.2f} EUR entsprechen {dollar_betrag:.2f} USD.")
###############

# Aufgabe 7 Fstrings
name = input("Gib deinen Namen ein: ")
alter = int(input("Gib dein Alter ein: "))
aktuelles_jahr = datetime().year
jahr_100 = aktuelles_jahr + (100 - alter)
print(f"Hallo {name}, du wirst im Jahr {jahr_100} 100 Jahre alt sein.")
