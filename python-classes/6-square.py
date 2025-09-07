#!/usr/bin/python3
"""Defines a class Square with size and position"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square

        Args:
            size (int): The size of the square (default is 0)
            position (tuple): The position of the square (default is (0, 0))
        """
        self.size = size      # uses setter for validation
        self.position = position  # uses setter for validation

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation"""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # considering position"""
        if self.__size == 0:
            print("")
            return

        # print newlines for vertical position
        for _ in range(self.__position[1]):
            print("")

        # print each line of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
