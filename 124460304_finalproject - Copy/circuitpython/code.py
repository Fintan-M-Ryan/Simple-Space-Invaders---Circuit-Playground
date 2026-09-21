import time
from adafruit_circuitplayground import cp
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import usb_hid
from sensorlightdisplay import SensorLightDisplay

keyboard = Keyboard(usb_hid.devices)
sld = SensorLightDisplay(brightness=0.3)

while True:
    x, y, z = cp.acceleration

    # movement control
    if x < -3:
        keyboard.press(Keycode.LEFT_ARROW)
        keyboard.release(Keycode.RIGHT_ARROW)
    elif x > 3:
        keyboard.press(Keycode.RIGHT_ARROW)
        keyboard.release(Keycode.LEFT_ARROW)
    else:
        keyboard.release(Keycode.LEFT_ARROW)
        keyboard.release(Keycode.RIGHT_ARROW)

    # fire dart with button A
    if cp.button_a:
        keyboard.press(Keycode.SPACE)
        keyboard.release(Keycode.SPACE)

    if cp.button_b:
        keyboard.press(Keycode.E)
        keyboard.release(Keycode.E)

    # LED feedback
    sld.advanced_control_feedback(x)

    time.sleep(0.05)
