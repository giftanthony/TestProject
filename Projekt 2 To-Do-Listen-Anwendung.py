# To-Do Liste App
import os
def datei_laden():
    return open("todo.txt").read().splitlines() if os.path.exists("todo.txt") else []
def aufgaben_anzeigen():
    print("\nAufgaben:")
    for i, aufgabe in enumerate(aufgaben, 1):
        print(f"{i}. {aufgabe}")


aufgaben = datei_laden()

while True:
    print("\nHallo, bitte geben Sie aus der Option die Nummer ein, die Sie bearbeiten möchten und ‚done‘ wenn Sie mit "
          "der Berechnung fertig sind. \n1. Hinzufügen\n2. Anzeigen\n3. Bearbeiten\n4. Löschen")
    try:
        wahl = input("Bearbeitungsoption von (1-4): auswählen ")

        if wahl == "1":
            aufgaben.append(input("Neue Aufgabe: "))
        elif wahl == "2":
            aufgaben_anzeigen()
        elif wahl in ["3", "4"]:
            aufgaben_anzeigen()
            index = int(input("Aufgabennummer: ")) - 1
            if wahl == "3":
                aufgaben[index] = input("Neuer Text: ")
            else:
                aufgaben.pop(index)
        elif wahl == "done":
            open("todo.txt", "w").write("\n".join(aufgaben))
            break

    except (ValueError, IndexError):
        print("Ungültige Eingabe!")
    except Exception:
        print("Fehler aufgetreten!")