i = 1
while i <= 10:
    print(i)
    i += 1
o = 10
while o >= 1:
    print(o)
    o -= 1

username = ""
password = ""
counter = 0
while username != "rmount" or password != "pass":
    username = input("Please enter username: ")
    password = input("Password: ")
    counter += 1
    if counter > 3:
        print(f"You've tried too many times [{counter}]")
        break
if counter <= 3:
    print("Welcome!")
