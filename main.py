import random
import PySimpleGUI as sg

choices = ["rock", "paper", "scissors"]
winCount = 0
lossCount = 0   

def play_round():
    global winCount, lossCount
    loop = True

    while loop:
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

def render_gui(fun_window):


    # Create an event loop
    while True:
        event, values = fun_window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Quit" or event == sg.WIN_CLOSED:
            break

    fun_window.close()

def setup_gui():
    sg.theme('DarkAmber')  # Add a touch of color
    layout_column = [
                [sg.Text("Your choice: ", justification='center', size=(100,1))],
                [sg.Button("Rock" , size=(10,1)), sg.Button("Paper", size=(10,1)), sg.Button("Scissors",  size=(10,1))],
                [sg.Button("Quit", size=(10,1))]
             ]
    layout = [[sg.Column(layout_column, element_justification='center')]]

    sgWindow = sg.Window("Rock, Paper, Scissors", layout, size=(500, 500), margins=(5, 5), resizable=True, finalize=True, grab_anywhere=True)
    return sgWindow

if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors!")
    print("To start type out your choise, to quit type 'quit'")

    window = setup_gui()
    render_gui(window)

    play_round()


    winRate = round(winCount/ (lossCount + winCount) * 100, 1)
    print(f"Goodbye, you won {winCount} times and lost {lossCount} times, this gives you a winrate of {winRate} percent")

