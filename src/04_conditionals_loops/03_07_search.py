'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

while True:
    try:
        user_input = int(input("Give me a number between 1 and 1.000.000.000"))
        break
    except ValueError:
        print("You should enter a NUMBER.")

while user_input < 1 or user_input > 1000000000:
    user_input = input("That's an incorrect input. Give me a number between 1 and 1.000.000.000")