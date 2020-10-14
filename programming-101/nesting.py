name = input("What is your name?")

length = len(name)
print(length)

if length > 3:
    if length < 10:
        if length == 4:
            #even if one block lower
            print("Perfect Length!")
        else:
            print("It's an ok length")

        print(f"Welcome {name}")
    else:
        print("That's way too long partner")
else:
    print(f"{length} is too few characters")