import Adafruit_BBIO.GPIO as GPIO
import requests
from time import sleep


NORTH_LED = "P9_11"
EAST_LED = "P9_13"
WEST_LED = "P9_14"
SOUTH_LED = "P9_12"
GPIO.setup(NORTH_LED, GPIO.OUT)
GPIO.setup(EAST_LED, GPIO.OUT)
GPIO.setup(WEST_LED, GPIO.OUT)
GPIO.setup(SOUTH_LED, GPIO.OUT)


locations = {"BODØ": "lat=62.29&lon=14.18",
             "NARVIK": "lat=68.43&lon=17.35",
             "TROMSØ": "lat=69.66&lon=18.63",
             "OSLO": "lat=59.89&lon=10.50"
             }

for locaction in locations:
    print(locaction)

choice = input("Velg en av alternativene over for værmelding: ")

url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?"+locations[str.upper(choice)]
# get weather from YR API
request = requests.get(url)
weather_json = request.json()

geometry = weather_json["geometry"]
properties = weather_json["properties"]
coordinates = geometry["coordinates"]
timeseries = properties["timeseries"]
meta = properties["meta"]
units = meta["units"]
time = timeseries[0]["time"]
data = timeseries[0]["data"]
instant = data["instant"]
details = instant["details"]
next_12_hours = data["next_12_hours"]
n12h_summary = next_12_hours["summary"]
symbol_code = n12h_summary["symbol_code"]


# Print weather forecast and blink LEDs corresponding to wind direction
print("\nVæret i ", str.capitalize(choice), " den, ", time[:10], " klokken", time[11:16])
print("Temperatur: ", details["air_temperature"], units["air_temperature"])
cloud_coverage = details["cloud_area_fraction"], "% skydekke"''

if details["cloud_area_fraction"] >= 70.0:
    print("Det er overskyet, med ", cloud_coverage)
elif 35 <= details["cloud_area_fraction"] <= 70:
    print("Det er delvis skyet, med ", cloud_coverage)
else:
    print("Det er lettskyet, med ", cloud_coverage)


def blink_led(led_1, led_2):
    GPIO.output(led_1, GPIO.HIGH)
    if led_2 is not None:
        GPIO.output(led_2, GPIO.HIGH)
    sleep(5)
    GPIO.output(led_1, GPIO.LOW)
    if led_2 is not None:
        GPIO.output(led_2, GPIO.LOW)
    GPIO.cleanup


# blink med lys i den vindretning som gjelder.
wind = details["wind_from_direction"], units["wind_from_direction"], details["wind_speed"], units["wind_speed"]

if details["wind_from_direction"] <= 45:
    print("Vind fra nord", wind)
    blink_led(NORTH_LED, None)
elif details["wind_from_direction"] <= 90:
    print("Vind fra øst", wind)
    blink_led(EAST_LED, None)
elif details["wind_from_direction"] <= 135:
    print("Vind fra sør-øst,", wind)
    blink_led(SOUTH_LED, EAST_LED)
elif details["wind_from_direction"] <= 180:
    print("Vind fra sør,", wind)
    blink_led(SOUTH_LED, None)
elif details["wind_from_direction"] <= 225:
    print("Vind fra sør-vest", wind)
    blink_led(SOUTH_LED, WEST_LED)
elif details["wind_from_direction"] <= 270:
    print("Vind fra vest", wind)
    blink_led(WEST_LED, None)
elif details["wind_from_direction"] <= 315:
    print("Vind fra nord-vest,", wind)
    blink_led(NORTH_LED, WEST_LED)
else:
    print("Vind fra nord", wind)
    blink_led(NORTH_LED, None)
