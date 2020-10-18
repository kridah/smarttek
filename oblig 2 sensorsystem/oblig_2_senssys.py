import Adafruit_BBIO.ADC as ADC

# BPM = 60 * Fsampling / sampling_periods with Fsampling
from datetime import datetime

ADC.setup()

sensor_path = "/sys/class/hwmon/hwmon0/temp1_input"
timestamp = datetime.now().timestamp()
while True:
    ADC.read("P9_40")
    with open(sensor_path, 'r') as file:
        for temp in file:
            # skriv ut tid $1 (x) og motstand ($2) (y), temperatur ($3) (y)
            print("{:.3f}, {:.4f}, {}".format(
                datetime.now().timestamp() - timestamp,     # tid mellom hver måling
                ((ADC.read("P9_40") * 4096) / 1.8),
                float(temp) / 1000)
            )