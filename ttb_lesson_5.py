import Adafruit_BBIO.GPIO as GPIO
from time import sleep

LED_Top = "P9_11"
LED_Bottom = "P9_12"

GPIO.setup(LED_Top, GPIO.OUT)
GPIO.setup(LED_Bottom, GPIO.OUT)

delay = input("Hvor lenge det blinkes? ")
times = input("Hvor mange ganger skal det blinke?" )

for i in range(0, int(times)):
    print(i, ": High")
    GPIO.output(LED_Top, GPIO.HIGH)
    GPIO.output(LED_Bottom, GPIO.HIGH)
    sleep(int(delay))
    print("Low")
    GPIO.output(LED_Top, GPIO.LOW)
    GPIO.output(LED_Bottom, GPIO.LOW)
    sleep(int(delay))

GPIO.cleanup()
