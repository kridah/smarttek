import Adafruit_BBIO.ADC as ADC
from time import sleep
import csv

ADC.setup()
pin = ADC.read("P9_40")

while True:
    value = ADC.read_raw("P9_40")
    print("{0:.0f}".format(value))
    sleep(0.1)
