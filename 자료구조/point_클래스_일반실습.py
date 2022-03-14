import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return f"({self.x})"
    def getY(self):
        return f"({self.y})"
    def get(self):
        return f"({self.x}, {self.y})"
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    def setX(self):
        return (self.x).set()

p = Point(1, 2)
print(p.getX())
print(p.getY())
print(p.get())
p.move(3, 6)
print(p.setX())
