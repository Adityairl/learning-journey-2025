import random

computer = random.choice([1, -1, 0])

youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()
youDict = {"r": 1, "p": -1, "s": 0}

if youstr not in youDict:
    print("Invalid input")
else:
    you = youDict[youstr]
    choices = {1: "Rock", -1: "Paper", 0: "Scissors"}
    print(f"Computer chose: {choices[computer]}")
    print(f"You chose: {choices[you]}")

    if computer == you:
        print("It's a Tie!")
    elif (computer == 1 and you == 0) or (computer == -1 and you == 1) or (computer == 0 and you == -1):
        print("You Lose")
    else:
        print("You Win")
