import RPi.GPIO as GPIO

class Led:
    def __init__(self, pin):
        self.led_pin = pin
        GPIO.setup(self.led_pin, GPIO.OUT)

    def light_on(self):
        if not self.get_status():
            GPIO.output(self.led_pin, GPIO.HIGH)
    
    def light_off(self):
        if self.get_status():
            GPIO.output(self.led_pin, GPIO.LOW)

    def get_status(self):
        status = GPIO.input(self.led_pin)
        return status == GPIO.HIGH

