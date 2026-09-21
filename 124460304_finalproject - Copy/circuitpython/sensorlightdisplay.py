from adafruit_circuitplayground import cp

class SensorLightDisplay:
    BLACK = (0, 0, 0)

    def __init__(self, brightness):
        self.pixels = cp.pixels
        self.pixels.brightness = brightness
        self.NUM_PIXELS = len(self.pixels)

    def advanced_control_feedback(self, acceleration_x):
        if acceleration_x < -9.81 or acceleration_x > 9.81:
            return

        for i in range(self.NUM_PIXELS):
            self.pixels[i] = self.BLACK

        if -3 <= acceleration_x <= 3:
            self.pixels.show()
            return

        # unified colour gradient (green → red)
        strength = min(abs(acceleration_x) / 9.81, 1.0)
        red = int(255 * strength)
        green = 255 - red
        colour = (red, green, 0)

        if acceleration_x < -3:
            for i in range(0, 5):
                self.pixels[i] = colour

        elif acceleration_x > 3:
            for i in range(5, 10):
                self.pixels[i] = colour

        self.pixels.show()
