import random

word_list = ["Ardvark","Baboon","Camel","Cow","Donkey"]
chosen_word = random.choice(word_list).lower()
print(chosen_word)
guess = input("Guess a letter: ").lower()
print(guess)

# check is it in the guessed letter

if guess in chosen_word:
    print("yes")
