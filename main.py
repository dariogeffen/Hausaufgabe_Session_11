import datetime
import json
import random

from datetime import datetime

secret = random.randint(1,30)
current_time = datetime.now()
attempts = 0
scores = []
x=0

print("-------------------------------------------------------------")
print("High Scores:")

#display highscores
with open("scores.json","r") as file:
    scores = json.loads(file.read())
    sort_scores = sorted(scores, key=lambda i: i['attempts'])
    while x < 3:
        entries = sort_scores[x]
        t=entries['date']
        t=datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f')
        print(f"{entries['name']}'s Score am {t.day}.{t.month}.{t.year}: {entries['attempts']}")
        x += 1

print("Schaffst du es die Zahl mit weniger Versuchen zu erraten?!!")
print("-------------------------------------------------------------")
name = input("Bitte Namen eingeben: ")
print("-------------------------------------------------------------")

while True:
    guess = int(input("Bitte gib eine Zahl ein: "))
    attempts += 1

    if guess == secret:
        print(f"Gewonnen, {guess} war die richtige Zahl!")
        print(f"Du hast {attempts} Versuche gebraucht, {name}!")
        wrong_guesses = attempts - 1

        with open ("scores.json", "w") as file:
            score_data = {"attempts": attempts, "date": str(current_time), "name":(name), "wrong_guesses":(wrong_guesses)}
            scores.append(score_data)
            file.write(json.dumps(scores))

        break
    elif guess > secret:
        print(f"Die gesuchte Zahl ist kleiner als {guess}")
    elif guess < secret:
        print(f"Die gesuchte Zahl ist größer als {guess}")

