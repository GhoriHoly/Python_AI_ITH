import random

list_items = ["Rock", "Papper","Scissor"]

def generate_guess():
    user_guess = input("Type Rock/Papper/Scissor: ").lower()
    computer_guess = random.choice(list_items).lower()
    print(f"You guessed: {user_guess}  and the computer guessed: {computer_guess}")
    return user_guess, computer_guess


def check_winner(u_guess, c_guess):
    if u_guess == c_guess:
        print("This is a tie!")
    elif u_guess == 'rock':
        if c_guess == 'papper':
            print("You Lose!")
        else:
            print("You win!")
    elif u_guess == 'papper':
        if c_guess == 'rock':
            print("You win!")
        else:
            print("You lose")
    elif u_guess == 'scissor':
        if c_guess == 'rock':
            print("You lose!")
        else:
            print("You win!")




game_on = True
print("Welcome to the Rock Papper Scissor game!")
while game_on:
    u_guess, c_guess = generate_guess()
    check_winner(u_guess,c_guess)

    user_choice = input("Do you want to play again? Yes/No ").lower()

    if user_choice == 'no':
        game_on = False
