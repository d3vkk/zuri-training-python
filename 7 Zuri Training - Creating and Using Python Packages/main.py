
import random

def determine_winner(cpu_choice, players_choice):
    if cpu_choice == 'R' and players_choice == 'P':
        return 'Player'
    elif cpu_choice == 'P' and players_choice == 'R':
        return 'CPU'
    elif cpu_choice == 'S' and players_choice == 'R':
        return 'Player'
    elif cpu_choice == 'R' and players_choice == 'S':
        return 'CPU'
    elif cpu_choice == 'P' and players_choice == 'S':
        return 'Player'
    elif cpu_choice == 'S' and players_choice == 'P':
        return 'CPU'
    elif cpu_choice == players_choice:
        return 'NONE'

def translate_choices(choice):
    if choice == 'R':
        return 'Rock'
    elif choice == 'P':
        return 'Paper'
    elif choice == 'S':
        return 'Scissors'

def play_rps(players_choice):
    cpu_choice = random.choice(['R', 'P', 'S'])
    winner = determine_winner(cpu_choice, players_choice)

    print("Player(" + translate_choices(players_choice) + ") : CPU(" +  translate_choices(cpu_choice) +")")
    if winner == 'NONE':
        print("No One Wins. Play Again! \n")
        return False
    else:
        print(winner + " Wins! \n")
        return True


def start_game():
    while True:
        print("Rock, Paper and Scissors game with your CPU!")
        players_choice = str(input("Enter 'R', 'P' or 'S': "))

        if players_choice == "R" or players_choice == "P"  or players_choice == "S":
            dont_play_again = play_rps(players_choice)
            if dont_play_again == True:
                break
        else:
            print("Invalid choice. Enter a valid choice please (use uppercase letters) \n")

start_game()
