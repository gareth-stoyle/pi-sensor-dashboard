import RPi.GPIO as GPIO
from motion_sensor import MotionSensor # KS0052
import time
import Adafruit_DHT as DHT # DHT11 sensor


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)

    motion_sensor = MotionSensor(motion_pin=4, led_pin=17)
    dht_sensor = DHT.DHT11
    dht_pin = 21

    try:
        while True:
            humidity, temp = DHT.read(dht_sensor, dht_pin)
            if humidity and temp:
                print("Temperature = {0:0.1f}C, Humidity = {1:0.1f}".format(temp, humidity))
            else:
                print("Sensor failure")

            motion_sensor.set_status()
            if motion_sensor.get_status():
                print("Motion detected")
            else:
                print("Motion not detected")
            time.sleep(4)
    except KeyboardInterrupt:
        GPIO.cleanup()