import Adafruit_BBIO.ADC as ADC

# Temperature = ((Vout in mV) – 500mV) / 10
# https://elinux.org/EBC_Exercise_31_Dallas_1-Wire

ADC.setup()
pin = "P9_12"
sensor_path = "/sys/class/hwmon/hwmon0/temp1_input"
with open(sensor_path, 'r') as file:
    for temp in file:
        print(float(temp)/1000)