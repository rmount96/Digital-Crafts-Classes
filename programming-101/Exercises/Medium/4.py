height = int(input("height? "))
width = int(input("width? "))

print("* " * width)
while height > 0:
    print(f"*" + " " + {width} + " *")
    height -= 1

print("*" * width)