#import Adafruit_BBIO.GPIO as GPIO
import digitalio
import board
from time import sleep

led = digitalio.DigitalInOut(board.P8_10)
led.direction = digitalio.Direction.OUTPUT


for i in range(0, 5):
    led.value = True
    print("High")
    sleep(0.5)
    led.value = False
    print("Low")
    sleep(0.5)
