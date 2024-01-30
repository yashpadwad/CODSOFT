import random
print("Hey Player!")
print("Welcome to the traditional rock , paper , scissors game")
def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    return choice
def get_machine_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def determine_winner(user_choice, machine_choice):
    if user_choice == machine_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and machine_choice == 'scissors') or (user_choice == 'scissors' and machine_choice == 'paper') or (user_choice == 'paper' and machine_choice == 'rock'):
        
        return "You win!"
    else:
        return "Machine wins!"
def play():
    user_choice = get_user_choice()
    print("Your choice:", user_choice)
    machine_choice = get_machine_choice()
    print("Machine's choice:", machine_choice)
    print(determine_winner(user_choice, machine_choice))

play()
playagain = input("Wanna go for another round..yes/no?")
if(playagain=="yes") :
    play()
else :
    print("Better luck next time")


