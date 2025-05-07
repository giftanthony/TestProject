x = 10

def aenders_x():
    global x
    x = x - 3 # 10 -> 7
    print(x)
print("vor Funktion", x)
aenders_x()
print("nach Funktion", x)