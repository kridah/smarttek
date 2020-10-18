import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

led = "P8_10"
GPIO.setup(led, GPIO.OUT)
ADC.setup()

# BPM = 60 * Fsampling / sampling_periods with Fsampling

#pin = ADC.read_raw("P9_40")
timer = 0.0
voltage = 0
GPIO.output(led, GPIO.HIGH)
while timer <= 10:
    ADC.read("P9_40")
    timer += 0.1
    # skriv ut tid $1 (x) og motstand ($2) (y)
    print("{:.3f}, {:.4f}".format(timer, ((ADC.read("P9_40") *4096) / 1.8)))
    sleep(0.1)  # 10 avlesninger i sekundet

GPIO.output(led, GPIO.LOW)
GPIO.cleanup()

##### GNUPLOT #####
# plot "hr.csv" using ($2/100) title "Raw-data" lt 7 lc 2 w l
# xlabel = "Tid"
# ylabel = "Motstand"