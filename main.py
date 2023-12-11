import random

choices = ["rock", "paper", "scissors"]


def main():
    loop = True
    winCount = 0
    lossCount = 0   

    while(loop):
        userInput = input("Your choice: ").lower()
        if userInput == "quit":
            winRate = round(winCount/ (lossCount + winCount) * 100, 1)
            print(f"Goodbye, you won {winCount} times and lost {lossCount} times, this gives you a winrate of {winRate} percent")
            break
        try:
            if userInput not in choices:
                raise TypeError("Choice is not valid")
            
            aiChoice = random.choice(choices)
            print(f"Computer chooses: {aiChoice}")

            winner = getWinner(userInput, aiChoice)
            if winner == 1:
                winCount+=1
                print("You Won!")
            elif winner == 0:
                lossCount+=1
                print("You Lost")
            else:
                print(winner)

        except(TypeError):
            print("Choice is not valid")
        except Exception as e:
            print(f"Error: {e}")

def getWinner(userChoice, aiChoice):
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
    main()