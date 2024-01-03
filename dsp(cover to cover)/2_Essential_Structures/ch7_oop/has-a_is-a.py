# OOP has 2 types of realtionships
# 1st (has-a relationship) is composition wherein an object contains another object
class Engine:
    pass


class Car:
    def __init__(self):
        self.engine = Engine()


## here one class has an instance of another class as a member.


# 2nd (is-a relationship) is inheritence wherein an object is derived from another objects.
class Animal:
    pass


class Dog(Animal):
    pass
