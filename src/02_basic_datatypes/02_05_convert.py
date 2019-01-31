'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

x=10
print(x)
y=float(x)
print(y)
z=x/y
print(z)
x=int(input('Give a number.'))
y=int(input('Give a second one.'))
print('These numbers multiplied gives you: ', x*y)
