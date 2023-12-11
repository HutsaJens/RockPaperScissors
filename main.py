import random

choices = ["rock", "paper", "scissors"]
winCount = 0
lossCount = 0   

def play_round():
    global winCount, lossCount
    loop = True

    while(loop):
        userInput = input("Your choice: ").lower()

        if userInput == "quit":
            return
        
        elif userInput not in choices:
            print("Invalid choice. Please enter one of the following choices: rock, paper, or scissors.")
            continue

        aiChoice = random.choice(choices)
        print(f"Computer chooses: {aiChoice}")

        outCome = getOutCome(userInput, aiChoice)
        if outCome == 1:
            winCount+=1
            print("You Won!")
        elif outCome == 0:
            lossCount+=1
            print("You Lost")
        else:
            print(outCome)


def getOutCome(userChoice, aiChoice):
    if userChoice == aiChoice:
        return "Draw"
    elif userChoice == "rock" and aiChoice == "scissors":
        return 1
    elif userChoice == "rock" and aiChoice == "paper":
        return 0
    elif userChoice == "paper" and aiChoice == "scissors":
        return 0
    elif userChoice == "paper" and aiChoice == "rock":
        return 1
    elif userChoice == "scissors" and aiChoice == "paper":
        return 1
    elif userChoice == "scissors" and aiChoice == "rock":
        return 0
    else:
        return "Unknown"


if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors!")
    print("To start type out your choise, to quit type 'quit'")

    play_round()

    winRate = round(winCount/ (lossCount + winCount) * 100, 1)
    print(f"Goodbye, you won {winCount} times and lost {lossCount} times, this gives you a winrate of {winRate} percent")

