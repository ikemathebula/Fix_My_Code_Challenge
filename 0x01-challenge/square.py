#!/usr/bin/python3
""" Square module """


class square():
    """ Defines a square """

    def __init__(self, width=0, height=0):
        """ Initializes square """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width of the square """
        return self.__width

    @property
    def height(self):
        """ Height of square """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets width of the square """
        if type(value) != int:
            raise TypeError("Width must be an integer")
        elif value < 1:
            raise ValueError("Width must be greater than 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ Sets height of thesquare """
        if type(value) != int:
            raise TypeError("Height must be an integer")
        if value < 1:
            raise ValueError("Height must be greater than 0")
        else:
            self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Sting representation of the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
