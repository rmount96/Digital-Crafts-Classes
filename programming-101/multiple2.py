pet_name = input("What is your pet's name?")
length = len(pet_name)


if length < 3:
    print(f"{pet_name} is too short")
elif pet_name == "Shadow":
    print("El Gato Diablo!")
elif pet_name == "Daisy":
    print("Good dog")
else:
    print(f"AWWWW sweet {pet_name}")

#cant print only for shadow and daisy
