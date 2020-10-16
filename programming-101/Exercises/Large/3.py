print("I am thinking of a number between 1 and 10")
secret_number = '' 

while secret_number != '5':
    if secret_number > '5':
        print("Too high!")
    elif secret_number < '5':
        print("Too low!")
    secret_number = input("What's the number? ")

if secret_number == '5':
    print("Yes! You win!")