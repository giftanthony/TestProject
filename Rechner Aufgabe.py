def rechner():
    while True:
        print("\nHello, Geben Sie ‚Berechnungsoption‘ ein, und ‚done‘ wenn Sie mit der Berechnung fertig "
              "sind \n1. Addition (+)\n2. Subtraktion (-)\n3. Multiplikation (*)\n4. Division (/).")
        wahl = input("Berechnungsoption von (1-4) auswählen: ")

        if wahl == "done":
            print("Programm beendet.")
            return
        elif wahl in ["1", "2", "3", "4"]:
            try:
                a = float(input("Gib die erste Zahl ein: "))
                b = float(input("Gib die zweite Zahl ein: "))

                if wahl == "1":
                    print("Ergebnis:", a + b)

                    while True:
                        choice = input("Tolle Arbeit, bitte geben Sie „done“ ein, um die Rechnung "
                                       "zu beenden und „neu“, um mit der neuen Berechnung fortzufahren.: ").lower()
                        if choice == "neu":
                            break
                        elif choice == "done":
                            print("Programm beendet.")
                            return
                        else:
                            print("Ungültige Eingabe! Bitte 'continue' oder 'done' eingeben.")
                elif wahl == "2":
                    print("Ergebnis:", a - b)
                    while True:
                        choice = input("Tolle Arbeit, bitte geben Sie „done“ ein, um die Rechnung "
                                       "zu beenden und „neu“, um mit der neuen Berechnung fortzufahren.: ").lower()
                        if choice == "neu":
                            break
                        elif choice == "done":
                            print("Programm beendet.")
                            return
                        else:
                            print("Ungültige Eingabe! Bitte 'continue' oder 'done' eingeben.")
                elif wahl == "3":
                    print("Ergebnis:", a * b)
                    while True:
                        choice = input("Tolle Arbeit, bitte geben Sie „done“ ein, um die Rechnung "
                                       "zu beenden und „neu“, um mit der neuen Berechnung fortzufahren.: ").lower()
                        if choice == "neu":
                            break
                        elif choice == "done":
                            print("Programm beendet.")
                            return
                        else:
                            print("Ungültige Eingabe! Bitte 'continue' oder 'done' eingeben.")
                elif wahl == "4":
                    if b == 0:
                        print("Fehler: Division durch 0 nicht erlaubt!")
                    else:
                        print("Ergebnis:", a / b)
                        while True:
                            choice = input("Tolle Arbeit, bitte geben Sie „done“ ein, um die Rechnung "
                                           "zu beenden und „neu“, um mit der neuen Berechnung fortzufahren.: ").lower()
                            if choice == "neu":
                                break
                            elif choice == "done":
                                print("Programm beendet.")
                                return
                            else:
                                print("Ungültige Eingabe! Bitte 'continue' oder 'done' eingeben.")
            except:
                print("Ungültige Eingabe! Bitte nur Zahlen eingeben.")
        else:
            print("Ungültige Option! Bitte wähle 1-4.")

rechner()