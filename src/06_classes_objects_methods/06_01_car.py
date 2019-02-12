'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def accelarate(self):
        self.max_speed += 5

    def __str__(self):
        print(f'This car is a {model} from {year} and it drives {max_speed}')

punto = Car('Fiat Punto', 2015, 200)
fiesta = Car('Ford Fiesta', 2000, 160)

punto.accelarate()
punto.accelarate()

print(punto.max_speed)
print(fiesta.model)