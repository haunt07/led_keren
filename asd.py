from module import led
from config import pin_out
import time

led_1 = led.setup(pin_out.led1['pin'])
led_2 = led.setup(pin_out.led2['pin'])

try:
    while 1:
        led_1.on()
        led_2.off()
        time.sleep(1)
        led_1.off()
        led_2.on()
        time.sleep(1)
except e:
    pass
