'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''


while True:
    try:
        user_input = int(input("Give me a number between 1 and 1.000.000.000"))
        break
    except ValueError:
        print("You should enter a NUMBER.")

while user_input < 1 or user_input > 1000000000:
    user_input = input("That's an incorrect input. Give me a number between 1 and 1.000.000.000")

if user_input%3 == 0:
    print("Your number is divisible by 3.")
else:
    print("Your number is not divisible by 3.")