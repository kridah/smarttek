import Adafruit_BBIO.ADC as ADC

# måler temperatur ca hvert 0.8 sekund
from datetime import datetime

ADC.setup()

sensor_path = "/sys/class/hwmon/hwmon0/temp1_input"
timestamp = datetime.now().timestamp()
timer = 0
   # hr =  (ADC.read("P9_40") * 4096) / 1.8
with open(sensor_path, 'r') as file:
    for temp in file:
    # skriv ut tid $1 (x) og motstand ($2) (y), temperatur ($3) (y)
        print("{:.3f}, {:.4f}, {}".format(
            datetime.now().timestamp() - timestamp,     # tid mellom hver måling
            ((ADC.read("P9_40") * 4096) / 1.8),
            float(temp) / 1000)
        )
