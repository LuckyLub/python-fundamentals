'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''

while True:
    try:
        first = int(input('Give a number.'))
        break
    except ValueError:
        print("You should enter a NUMBER.")

while True:
    try:
        second = int(input(f'Give another number. It must be greater than your first number: {first}.'))
        break
    except ValueError:
        print("You should enter a NUMBER.")

total = 0
for i in range(first, second+1):
    total += i

print(f'The total sum of all the numbers between {first} and {second} equals {total}.')