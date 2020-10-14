age = int(input("How old are you?\n"))
if int(age) == 25:
    print("Get your own insurance")
elif age < 25:
    print("You might be on your parents' insurance")
else:
    print("You should definitely get your own insurance")