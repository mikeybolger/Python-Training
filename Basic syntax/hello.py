# This program says hello world and asks for my name

print("Hello world")

print("What is your name?") # Ask for their name
myName = input()
print("It is good to meet you, " + myName)
print("The length of your name is: ")
# Len takes the string argument and evaluates to the integer value for the lenght of the name 
print(str(len(myName)) + " characters")

print("What is your age?") # Ask for their age
myAge = input()
print("Your age is " + myAge)
print("You will be " + str(int(myAge) +1) + " in a year")
