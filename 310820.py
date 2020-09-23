import Adafruit_BBIO.GPIO as GPIO
from time import sleep
path = "/sys/class/leds/beaglebone:green:usr1/brightness"
f = open(path, "w")

for i in range(0, 3):
    f = open(path, "w")
    f.write("1")
    f.close()
    sleep(2)
    f = open(path, "w")
    f.write("0")
    f.close()
    sleep(2)

