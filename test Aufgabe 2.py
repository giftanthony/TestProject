import berechnungsmodul as bm  # 'import' and 'as' are keywords

a = 3
b = 4

if a == 4 and b == 4:  # 'if', 'and' are keywords
    print("a und b haben den Wert 4")  # 'print' is a built-in function, not a keyword
    bm.berechne_variante_x(a, b)  # Fixed spaces in function call
else:  # 'else' is a keyword
    print("a und b haben nicht gemeinsam den Wert 4")  # 'print' is a built-in function
    bm.berechne_variante_y(a, b)  # Fixed spaces in function call