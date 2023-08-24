import random
from art import logo

HARD_LEVEL = 5
EASY_LEVEL = 10

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")
answer = random.randint(0, 100)
print(f"Pssst, the correct answer is {answer}")
difficulty_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty_mode == 'easy':
    attempts = EASY_LEVEL
else:
    attempts = HARD_LEVEL

game_ended = False
while attempts > 0 or not game_ended:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer:
        print(f"You got it! The answer was {answer}. You only needed {attempts} attempts.")
        game_ended = True
    elif guess < answer:
        attempts -= 1
        print("Too low")
        if attempts != 0:
            print("Guess again.")
    else:
        attempts -= 1
        print("Too high")
        if attempts != 0:
            print("Guess again.")
    if attempts == 0:
        game_ended = True

if attempts == 0:  
    print("You've run out of guesses, you lose.")
