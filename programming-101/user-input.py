name = input("Name Please:")
subject = input("Favorite Subject:")

age = input("How old are you?")

#since age is defined as int, can't input a string
if int(age) >= 21:
    print("Grab a Beer?")

print(f"You said your name is {name}")

