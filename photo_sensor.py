import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time

sensor_pin = "P9_40"
out_pin = "P9_23"

GPIO.setup(out_pin, GPIO.OUT)
ADC.setup()

print("Reading\t\tVolts")

while True:
    reading = ADC.read(sensor_pin)
    volts = reading * 1.800
    print("%f\t%f" % (reading, volts))
    time.sleep(1)
    if volts < 1.0:
        GPIO.output(out_pin, GPIO.HIGH)
    else:
        GPIO.output(out_pin, GPIO.LOW)

ADC.cleanup()
GPIO.cleanup()
