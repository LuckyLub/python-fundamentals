'''def print_names(people):
    l1 = len(people)
    c1 = 0

    while c1 < l1:
        to_print = ""
        person = people[c1]
        l2 = len(person)
        c2 = 0
        while c2 < l2:
            name = person[c2]
            to_print += name + " "
            c2 +=1
        print(to_print)
        c1 += 1

print_names([['John', 'Smith'],['Mary', 'Keyes'],['Jane', 'Doe'],['Angus']])'''

class Class1:
    def __init__(self):
        self.x = 5

class Class2(Class1):

    def __init__(self):
        super().__init__()
        self.y = 1

b = Class2()
print(b.y + b.x)