# 10/0 ##error, can't divide by 0
my_num = input("Give me a number: ")

try:
    my_num = int(my_num)
    print(100 / my_num)
except ZeroDivisionError:
    print("You tried to divide by zero")
except TypeError:
    print("You did something wrong with the type")
except ValueError:
    print("You didnt give a number")

