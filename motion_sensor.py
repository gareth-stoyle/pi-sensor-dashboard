#KS0052 motion sensor
import RPi.GPIO as GPIO
from led import Led

class MotionSensor:
	def __init__(self, led_pin, motion_pin):
		self.led = Led(led_pin)
		self.motion_pin = motion_pin
		GPIO.setup(self.motion_pin, GPIO.IN)
    
	def get_status(self):
		status = GPIO.input(self.motion_pin)
		return status == GPIO.HIGH

	def set_status(self):
		if self.get_status():
			self.led.light_on()
		else:
			self.led.light_off()


