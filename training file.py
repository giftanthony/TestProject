input = ("Wie heiß du")
input = ("f Hello {name} how are i help you")


lngjähriges_mittel = 18.23
print ("Programm zur Berechnung einer Durchschnittstemperatur \ n")
print ("Geben Sie bitte drei Temperaturwerte in ° C ein!")
temperatur1 = float (input ("1. Wert:"))
temperatur2 = float (input ("2. Wert:"))
temperatur3 = float (input ("3. Wert:"))
durchschnitt = (temperatur1 + temperatur2 + temperatur3)/3
print ("Sie haben folgende Temperaturen eingeben: { 0 } ° C, { 1 } ° C, { 2 } ° C"
       .format (temperatur1, temperatur2, temperatur3))
print ("Die Durchschnittstemperatur beträgt: {0:. 2f} ° C"
       .format (durchschnitt))
if durchschnitt >= langjähriges_mittel:
    if durchschnitt > langjähriges_mittel:
        print ("Die Temperatur liegt über dem langjährigen Mittel")
    else:
        print ("Die Temperatur entspricht dem langjährigen Mittel")
else:
    print ("Die Temperatur liegt unter dem langjährigen Mittel")
except Exception as e:
                     print (" Es ist folgender Fehler aufgetreten: \ n“ + e. args [0])


auswahl = int (input (" Geben Sie eine ganze Zahl ein:"))
if auswahl == 1: print (" Es wurde eine 1 eingeben.")
elif auswahl == 2:
    print (" Es wurde eine 2 eingeben.")
elif auswahl == 3:
    print (" Es wurde eine 3 eingeben.")
elif auswahl < 1 or auswahl > 3:
    print (" Es wurde keine 1, 2 oder 3 eingeben.")
#################

zahl = float(input(" Geben Sie eine Gleitkommazahl ein:"))
if zahl >= 10.0 and zahl <= 20.0:
    print(" Die Zahl {0} liegt im Bereich von 10 bis 20 ".format(zahl))
else:
    print(" Die Zahl {0} liegt nicht im Bereich von 10 bis 20 ".format(zahl))
