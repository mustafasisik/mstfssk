from __future__ import print_function


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "%s , %d " % (self.name, self.age)

    def __eq__(self, b):
        return self.age == b.age

    def __lt__(self, b):
        return self.age < b.age

    def __getattr__(self, x):
            return self.name

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age


b = Person("ahmet", 30)

c = Person("Mehmet", 37)

print(b.name)
print(b.sdsa)



