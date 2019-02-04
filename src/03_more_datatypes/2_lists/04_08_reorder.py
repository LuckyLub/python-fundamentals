'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

numbers=[]
sequence=[2,4,6,8,10,9,7,5,3,1]
ammount = 10
i=1

while i<=ammount:
    numbers.append(int(input(f'Give me a number! ({i} of {ammount})')))
    i += 1

for x in sequence:
    x=x-1
    print(numbers[x])