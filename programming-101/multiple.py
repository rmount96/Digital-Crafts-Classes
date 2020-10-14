name = input("What is your name?")
num = len(name)
## you can have multiple conditions here
if num > 3 and num < 15:
    if num ==4:
        print("perfect length!")
    else:
        print("It's an ok length")
    
    print (f"Welcome {name}")
else:
    print(f"{num} is not a good number of characters")

#if num < 3 or num > 15:
    print("This is valid")
#else:
    print("Normal lengthed name")
