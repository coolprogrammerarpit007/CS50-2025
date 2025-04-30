# Object Oriented Programming

import math

class Circle:
    def __init__(self,radius):
        self._radius = radius

    def area_of_cirle(self):
        return math.pi * self._radius * self._radius


circle1 = Circle(5)
area1 = circle1.area_of_cirle()
# print(f"Area of circle: {area1}")

# Class Attributes
class ObjectCounter:
    num_of_instances = 0

    def __init__(self):
        ObjectCounter.num_of_instances += 1


# ObjectCounter()
# ObjectCounter()
# ObjectCounter()
# ObjectCounter()
# ObjectCounter()
# ObjectCounter()
# print(ObjectCounter.num_of_instances)

# Instance Attributes

class Car:
    def __init__(self,make,model,year,color):
        self._make = make
        self._year = year
        self._model = model
        self._color = color
        self.standard = False
        self.speed = 0
        self.max_speed = 200


# toyota_camry = Car("Toyota","Camry",2000,"Silver")
john = {
        "name": "John Doe",
        "position": "Python Developer",
        "department": "Engineering",
        "salary": 80000,
        "hire_date": "2020-01-01",
        "is_manager": False,
}
class Record:
    """ Hold a record of data"""

john_record = Record()
for key,value in john.items():
    setattr(john_record,key,value)


# print(john_record.__dict__)