#!/usr/bin/python3
''' define a Rectangle '''


class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __str__(self):
        cat = []
        if self.width == 0 or self.height == 0:
            return ""
        else:
            for a in range(self.height):
                for b in range(self.width):
                    cat.append("{}".format(self.print_symbol))
                if a < self.height - 1:
                    cat.append("\n")
            return "".join(cat)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
