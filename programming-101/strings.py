message = "Hello world"
name = "Ryan"

print(name+" "+message)
combined = f"I want to say {message} to {name}"
print(combined)

print(f"I want to say {message} to {name}.")

new_string = "Hey this is %s, how are you?" % "Ryan"
print(new_string)

adj = "awesome"

print("%s my name is %s and I'm %s" % (message,name,adj))

haiku = "\tHaikus are easy.\nbut sometimes they don't make send.\n\tRefrigerator."
print(haiku)

print("yes","no","maybe")
