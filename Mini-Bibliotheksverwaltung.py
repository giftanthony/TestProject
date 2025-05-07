from multiprocessing.util import MAXFD

bibliothek = []
ausgeliehen = []


def buch_hinzufuegen():
    titel = input("Titel: ")
    autor = input("Autor: ")
    bibliothek.append({"titel": titel, "autor": autor})
    print(f"'{titel}' wurde hinzugefügt.")
    breakpoint()


def buch_ausleihen():
    titel = input("Titel des auszuleihenden Buches: ")
    for buch in bibliothek:
        if buch["titel"] == titel:
            bibliothek.remove(buch)
            ausgeliehen.append(buch)
            print(f"'{titel}' wurde ausgeliehen.")
            return
    print("Fehler: Buch nicht verfügbar!")


def buch_zurueckgeben():
    titel = input("Titel des zurückzugebenden Buches: ")
    for buch in ausgeliehen:
        if buch["titel"] == titel:
            ausgeliehen.remove(buch)
            bibliothek.append(buch)
            print(f"'{titel}' wurde zurückgegeben.")
            return
    print("Fehler: Buch nicht ausgeliehen!")


def buecher_anzeigen(liste, name):
    print(f"\n{name}:")
    for buch in liste:
        print(f"- {buch['titel']} ({buch['autor']})")


while True:
    print("\n1: Buch hinzufügen")
    print("2: Buch ausleihen")
    print("3: Buch zurückgeben")
    print("4: Verfügbare Bücher anzeigen")
    print("5: Ausgeliehene Bücher anzeigen")
    print("6: Beenden")

    try:
        wahl = input("Auswahl: ")

        if wahl == "1":
            buch_hinzufuegen()
        elif wahl == "2":
            buch_ausleihen()
        elif wahl == "3":
            buch_zurueckgeben()
        elif wahl == "4":
            buecher_anzeigen(bibliothek, "Verfügbare Bücher")
        elif wahl == "5":
            buecher_anzeigen(ausgeliehen, "Ausgeliehene Bücher")
        elif wahl == "6":
            break
        else:
            print("Ungültige Eingabe!")

    except:
        print("Fehler aufgetreten!")