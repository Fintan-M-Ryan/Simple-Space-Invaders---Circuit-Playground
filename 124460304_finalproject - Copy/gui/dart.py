import pygame

class Dart:
    __size = None

    def __init__(self, width, height, colour):
        self.__x = 0
        self.__y = 0
        self.__active = False
        Dart.__size = width
        self.__colour = colour
        self.__speed = height

    def draw(self, display):
        if self.__active:
            pygame.draw.rect(display, self.__colour,
                             [self.__x, self.__y, Dart.__size, Dart.__size])

    def activate(self):
        if not self.__active:
            self.__active = True

    def deactivate(self):
        if self.__active:
            self.__active = False

    def set_position(self, new_position):
        if not self.__active:
            self.__x = new_position[0]
            self.__y = new_position[1]

    def fire(self, dims):
        if self.__active:
            self.__y -= self.__speed
            if self.__y < 0:
                self.deactivate()

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_size(self):
        return Dart.__size

    def is_active(self):
        return self.__active
