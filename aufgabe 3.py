# Globale Variable x
from smtpd import usage

x = 10

# Funktion, die eine lokale Variable x definiert
def ändere_x():
    # Lokale Variable x
    x = 5
    print("Lokales x in der Funktion:", x)

# Ausgabe des globalen x vor dem Funktionsaufruf
print("Globales x vor dem Funktionsaufruf:", x)

# Aufruf der Funktion ändere_x()
ändere_x()

# Ausgabe des globalen x nach dem Funktionsaufruf
print("Globales x nach dem Funktionsaufruf:", x)


# Globale Variable x
x = 10

# Funktion, die die globale Variable x ändert
def ändere_x():
    global x  # Wir verwenden die globale Variable x
    x = 5     # Ändere den Wert der globalen Variable
    print("Globales x in der Funktion:", x)

# Ausgabe des globalen x vor dem Funktionsaufruf
print("Globales x vor dem Funktionsaufruf:", x)

# Aufruf der Funktion ändere_x()
ändere_x()

# Ausgabe des globalen x nach dem Funktionsaufruf
print("Globales x nach dem Funktionsaufruf:", x)