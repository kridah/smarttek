import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

GPIO.setup("P8_10", GPIO.OUT)
ADC.setup()

#pin = ADC.read_raw("P9_40")
timer = 0
voltage = 0
GPIO.output("P8_10", GPIO.HIGH)
while True:
    ADC.read("P9_40")
    #voltage = Decimal(ADC.read("P9_40") * 1.8)
    #print(voltage)
#    print("{:.6f} {:.4f}".format(ADC.read("P9_40"), ADC.read("P9_40") * 1.8))
    print("{:.0f}".format(ADC.read_raw("P9_40")))
    sleep(0.1)
    #timer += 0.1
