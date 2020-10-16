coins = 0
#print(f"You have {coins} coins.")
#more = input("Do you want another?") #yes also works
more = "yes"
while more == "yes":
    more = "no"
    #coins += 1
    print (f"You have {coins} coins ")
    more = input("Do you want another? ")
    if more == "yes":
        coins += 1
if more == "no":
    coins == coins
    print(f"You have {coins} coins")                