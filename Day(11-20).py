#Day 11
name = "Vaibhav"
friend = "Kajal"
anotherFriend = 'Shubhangi'
apple = '''He said,
Hi Vaibhav
Hey I am good
"I want to eat an apple'''
print("Hello, " + name)
print("Hello, " + friend)
print("Hello, " + anotherFriend)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

# reading the string using the for loop 
print("Let us use the for Loop\n")
for character in name:
    print(character)

for character in friend:
    print(character)

for character in apple:
    print(character)

# DAy 11 & 12
#Slicing and dicing operations on string.

names = "Vaibhav,Kajal"
print(names[0:7])
print(len(names))
fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4])
print(fruit[1:4])
print(fruit[:5])
print(fruit[0:-3])
print(fruit[-4:-2])

# Day 13

# Strings are immutable
a = "!!!!Vaibhav!!!!!!!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Vaibhav","Kajal")
print(a.split(" "))
Heading = "introduction to js"
print(Heading.capitalize())
