'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''

from datetime import date

class Action:


    def __init__(self, description = "What needs to be done.", owner = 'John Doe',  due_date = date(2000, 1, 1)):
        self.description = description
        self.owner = owner
        self.due_date = due_date

    def Postpone(self, days):
        year = self.due_date.year
        month = self.due_date.month
        day = self.due_date.day + days
        self.due_date = date(year, month, day)
        return f'The due date is now {self.due_date}'


    def Reschedule(self, date):
        self.due_date = date

    def __str__(self):
        return f"{self.owner} has to finish the action '{self.description}' before {self.due_date}."

class Person:

    def __init__(self, Surname = 'John or Jane', Name = 'Doe', Birthdate = date(2000, 1, 1), Country = "Antartica"):
        self.Surname = Surname
        self.Name = Name
        self.Birthdate = Birthdate
        self.Country = Country

    def Full_name(self):
        return self.Surname + " " + self.Name

    def __str__(self):
        return f'{self.Surname} {self.Name} is born on {self.Birthdate} and is from {self.Country}.'

class Location:

    def __init__(self, Placename = "Minas Tirith", Country = "Gondror", Continent = "Middle Earth"):
        self.Placename = Placename
        self.Country = Country
        self.Continent = Continent

    def __str__(self):
        return f'{self.Placename} is located in the country {self.Country} on the continent of {self.Continent}.'


place = Location()
john = Person()
act = Action()

print(place)
print(john)
print(act)

place2 = Location("Den Haag", "Netherlands", "Europe")
john2 = Person("Robert-Jan", "Lub", date(1991, 2, 23), place2.Country)
act2 = Action("Fly to Bali", john2.Full_name(), date(2019, 2, 15))

print(place2)
print(john2)
print(act2)

print(act2.Postpone(10))