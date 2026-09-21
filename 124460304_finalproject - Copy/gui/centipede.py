import pygame

class Centipede:
    __size = None

    def __init__(self, x, y, size, speed, colour):
        self.__x = x
        self.__y = y
        self.__speed = speed
        Centipede.__size = size
        self.__colour = colour
        self.__start_x = x
        self.__start_y = y
        self.__direction = 1

    def draw(self, display):
        pygame.draw.rect(display, self.__colour,
                         [self.__x, self.__y, Centipede.__size, Centipede.__size])

    def move(self):
        self.__x += self.__speed * self.__direction

    def collide(self, dims):
        window_width = dims[0]

        if self.__x + Centipede.__size >= window_width:
            self.__x = window_width - Centipede.__size
            self.__y += Centipede.__size
            self.__direction = -1

        if self.__x <= 0:
            self.__x = 0
            self.__y += Centipede.__size
            self.__direction = 1

    def relocate(self, dims):
        self.__x = self.__start_x
        self.__y = self.__start_y
        self.__direction = 1

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_size(self):
        return Centipede.__size

    def collide_with_dart(self, display_size, dart, event_list):
        if not dart.is_active():
            return

        cx, cy = self.__x, self.__y
        cw = ch = Centipede.__size

        dx, dy = dart.get_x(), dart.get_y()
        dw = dh = dart.get_size()

        if (dx < cx + cw and
            dx + dw > cx and
            dy < cy + ch and
            dy + dh > cy):

            dart.deactivate()
            self.relocate(display_size)
            event_list.add_event("Centipede hit by dart")
