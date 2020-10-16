import random
print("I am thinking of a number between 1 and 10")
number = random.randint(1, 10)
counter = 5
guess = ''


while counter != 0 and guess != number:
    print("What's the number?")
    guess = int(input(''))
    counter -= 1
    
    if guess > number:
        print(f"{guess} is too high\nYou have {counter} guesses left")
    if guess < number:
        print(f"{guess} is too low\nYou have {counter} guesses left")
    if guess == number:
        print("You win!")

