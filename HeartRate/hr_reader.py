import Adafruit_BBIO.ADC as ADC
from time import sleep

# BPM = 60 * Fsampling / sampling_periods with Fsampling

ADC.setup()
timer = 0.0
voltage = 0
while timer <= 20:
    ADC.read("P9_40")
    timer += 0.025
    # skriv ut tid $1 (x) og motstand ($2) (y)
    print("{:.3f}, {:.4f}".format(timer, ((ADC.read("P9_40") * 4096) / 1.8)))
    sleep(0.025)  # millisekunder mellom hver måling

##### GNUPLOT #####
# plot "hr.csv" using ($2/100) title "Raw-data" lt 7 lc 2 w l
# xlabel = "Tid"
# ylabel = "Motstand"
