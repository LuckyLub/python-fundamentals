'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


from datetime import date
# I don't understand how to import something from my owns scripts? So, copy paste:
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

class Author(Person):

    def __init__(self, Surname, Name, Birthdate, Country, *books):
        super().__init__(Surname, Name, Birthdate, Country)
        self.books = list(books)

    def __str__(self):
        return f'{self.Full_name()} wrote these book: {self.books}'

class Poet(Author):

    def __str__(self):
        return f'{self.Full_name()} wrote these poems: {self.books}'

class Songwriter(Author):

    def __str__(self):
        return "This person writes poetry."

Tolkien = Person('John Ronald Reuel', 'Tolkien', date(1892, 1, 3), "South Africa")
Tolkien = Author(Tolkien.Surname, Tolkien.Name, Tolkien.Birthdate, Tolkien.Country, "Lord of the Rings", "The Hobbit")

print(Tolkien)

Poe = Poet("Edgar Allan", "Poe", date(1809, 1, 19), "United States of America", "The Raven", "Annabel Lee"," The Bells")

print(Poe)