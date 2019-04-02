import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


class setup():
    pin = 0

    def __init__(self, pin=13):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin

    def on(self):
        print("on")
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        print("off")
        GPIO.output(self.pin, GPIO.HIGH)


if __name__ == "__main__":
    led_1 = setup(10)
    led_1.on()
