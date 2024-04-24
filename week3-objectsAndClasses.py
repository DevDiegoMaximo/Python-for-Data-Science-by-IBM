class Circle (object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def add_radius(self,r):
        self.radius = self.radius + r
        return (self.radius)#this is a class, classes has data attributes and methods

class Rectangle(object):
    def __init__(self, color, height, width):
        self.height = height
        self.color = color
        self.width = width

RedCircle = Circle(5,"red")
BlueRectangle = Rectangle("blue",5,5)

#this is the way to instance an opbject in python

print(RedCircle.radius)
print(BlueRectangle.color)

#this is the way to see the data in your object

RedCircle.add_radius(5)
print(RedCircle.radius)
#using methods

RedCircle.radius = 20
print(RedCircle.radius)


#Exercises
class Vehicle:
    color = "white"

    def __init__ (self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assing_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

V1 = Vehicle(150,25)
V1.assing_seating_capacity(5)
print(V1.color)

class Graph():
    def __init__(self, id):
        self.id = id
        self.id = 80

val = Graph(200)
print(val.id)