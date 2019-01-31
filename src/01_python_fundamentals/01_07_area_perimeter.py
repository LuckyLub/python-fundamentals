'''

Write the necessary code to display the area and perimeter of a rectangle that has a width of 2.4 and a height of 6.4.

'''

def rect_area(a,b):

    print('The area of the rectangular= ', a*b)

def rect_peri(a,b):
    print('The perimeter of the rectangular= ', a*2 + b*2)

a = int(input('What is the height of the rectangular'))
b = int(input('What is the width of the rectangular'))

rect_area(a,b)
rect_peri(a,b)