fragen = [
    {
        "frage": "Was ist die Hauptstadt von Deutschland?",
        "optionen": ["A: Berlin", "B: München", "C: Hamburg", "D: Köln"],
        "Die richtige Antwort ist": "A"
    },
    {
        "frage": "Wie viele einwohner hat berlin?",
        "optionen": ["A: 2 Millionen", "B: 6 Millionen", "C: 2,7Millionen", "D: 8 Millionen"],
        "Die richtige Antwort ist": "C"
    },
    {
        "frage": "Wer ist der bürgermeister von berlin?",
        "optionen": ["A: Kai Wegner", "B: Olaf Scholz", "C: Friedrich Merz", "D: Sahra Wagenknecht"],
        "Die richtige Antwort ist": "A"
    },
]

punkte = 0

print("Willkommen zum Quiz-Spiel!")
print("Beantworte die Fragen mit A, B, C oder D.\n")

for frage in fragen:
    print(frage["frage"])
    for option in frage["optionen"]:
        print(option)

    antwort = input("Deine Antwort: ").upper()

    if antwort == frage["Die richtige Antwort ist"]:
        print("Richtig!\n")
        punkte += 1
    else:
        print(f"Falsch! Die richtige Antwort war {frage['Die richtige Antwort ist']}.\n")

print(f"Quiz beendet! Deine Punktzahl: {punkte}/{len(fragen)}")