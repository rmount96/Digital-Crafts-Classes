print(1 == 2)   #False
print(1 <  2)   #True
print(1 >  2)   #False
print(1 >= 1)   #True
print(1 <= 2)   #True
print(1 != 1)   #False

a = 1
b = 2
print(a == b) #false

name = "Ryan"

print(name == "Ryan") #true
print(name == "Clint") #false
print(name != "ryan") #true
print(name > "a") #false
print(name > "A") #true

# capitalization takes priority over alphabitization
# != means not equal 

if 1 > 3:
    print("This will not be printed") #because condition is false
if 1 < 3:
    print("This will be printed") #because condition is true

#false statements
None
False
0
""
{} #only in python
[] #only in python

#true statements
True
1

did_do_something = True

if False:
    print("This will never print")

if True:
    print("This will always print")

if did_do_something:
    print("This will print because its true")