from abc import ABCMeta
class Shape:
    def perimeter(self):
        pass
class Square(Shape):
    def __init__(self, side_length):
        self.side = side_length
    def perimeter(self):
        print((self.side)*4)
side = input("Enter the Side of Square: \n")
Square = Square(side) 
Square.perimeter()       
             