import pygame

# A: Private variables store the Shooter's position, size, speed and colour.
#   Uses private variables to follow encapsulation and prevent accidental changes.

class Shooter:
    __size = None

    def __init__(self, x, y, size, speed, colour):
# B: sets the Shooter's starting position, size, speed and colour.
#    allows the object to be reused in different game setups.
        self.__x = x
        self.__y = y
        self.__speed = speed
        Shooter.__size = size
        self.__colour = colour


    def draw(self, display):
# D: Draws the Shooter on the display using the stored coordinates.
        pygame.draw.rect(display, self.__colour,
                         [self.__x, self.__y, Shooter.__size, Shooter.__size])

    def move_left(self):
# E: Moves the Shooter left by its speed and stops it at the left boundary.
        self.__x -= self.__speed
        if self.__x < 0:
            self.__x = 0

    def move_right(self, dims):
# F: Same as E but using the window width instead of zero (obviously)
        window_width = dims[0]
        self.__x += self.__speed
        if self.__x + Shooter.__size > window_width:
            self.__x = window_width - Shooter.__size   #using size instead of just position so it stops at the edge of the square/shooter rather than the center

# G: getters for the private variables
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_size(self):
        return Shooter.__size

    def get_speed(self):
        return self.__speed
