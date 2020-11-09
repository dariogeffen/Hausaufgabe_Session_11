import datetime
import json
import random

from datetime import datetime

secret = random.randint(1,30)
current_time = datetime.now()
attempts = 0
scores = []

print()


with open("scores.json","r") as file:
    scores = json.loads(file.read())

print("Jetzt geht's los!")
name = input("Bitte Namen eingeben: ")
print("______________________________")

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

        #with open("scores.json", "r") as file:
            #new_scores = json.loads(file.read())
            #sorted_scores = sorted(new_scores, key=lambda i: i['attempts'])
            #print(sorted_scores)


        break
    elif guess > secret:
        print(f"Die gesuchte Zahl ist kleiner als {guess}")
    elif guess < secret:
        print(f"Die gesuchte Zahl ist größer als {guess}")

