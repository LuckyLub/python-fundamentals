'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
from math import pi

def cyl_area(r):
    area = (r**2)*pi
    return area

def cyl_volume(h,r):
    volume = cyl_area(r) * h
    return volume

r = float(3.14)
height = float(5)

print('Area = ', cyl_area(r))

print('Volume =', cyl_volume(height, r))