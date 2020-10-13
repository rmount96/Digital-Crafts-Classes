name = "Ryan"
place = "Nebraska"
today = "Tuesday"
emotion = "well"
print(name+ " " +place)

haiku = f"\tHello {name} \nI hope that your {today} is going well. \n\tI'm really {emotion}"
print(haiku)


print(f"\tHello {name} \nI hope that your {today} is going well. \n\tI'm really {emotion} ")
print("\tHello %s \nI hope that your %s is going well. \n\tI'm really %s" % (name,today,emotion))