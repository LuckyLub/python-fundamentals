'''
Take in 10 numbers from the user. Place the numbers in a list.
Calculate the product of all of the numbers in the list.
Also, find the largest number in the list.

Print the results.

'''

numbers=[]
ammount = 10
i=1

while i<=ammount:
    numbers.append(int(input(f'Give me a number! ({i} of {ammount})')))
    i += 1

numbers_sum=sum(numbers)
numbers_max=max(numbers)

print(f'The largest number you gave is {numbers_max}. The total sum of all your numbers is {numbers_sum}.')