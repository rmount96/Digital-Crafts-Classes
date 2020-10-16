bill = input("How much was your bill? ")
x = float(bill)
bad = x * .10
fair = x * .15
good = x * .20

tipAmount = input("How was your service? ")
if tipAmount == "bad":
    total = x + bad
    print(f"Tip amount: ${bad:.2f}")
elif tipAmount == "fair":
    total = x + fair
    print(f"Tip amount: ${fair:.2f}")
elif tipAmount == "good":
    print(f"Tip amount: ${good:.2f}")
    total = x + good

print (f"Total Amount: ${total}")