import Adafruit_BBIO.GPIO as GPIO
from flask import Flask
from time import sleep
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask import render_template, request

LED_TOP = "P9_11"
LED_LEFT = "P9_14"
LED_RIGHT = "P9_13"
LED_BOTTOM = "P9_12"

GPIO.setup(LED_TOP, GPIO.OUT)
GPIO.setup(LED_LEFT, GPIO.OUT)
GPIO.setup(LED_RIGHT, GPIO.OUT)
GPIO.setup(LED_BOTTOM, GPIO.OUT)
app = Flask(__name__)

app.secret_key="thisissecret"

class BeagleForm(FlaskForm):
    top_led_button = SubmitField("Blink øverste LED")
    left_led_button = SubmitField("Blink venstre LED")
    right_led_button = SubmitField("Blink høyre LED")
    bottom_led_button = SubmitField("Blink nederste LED")


@app.route('/', methods=["GET", "POST"])
def index():
    form = BeagleForm()
    print(request.method)
    if request.form.get("top_led_button") == "top_led_button":
        blink_led(LED_TOP)
    if request.form.get("left_led_button") == "left_led_button":
        blink_led(LED_LEFT)
    if request.form.get("right_led_button") == "right_led_button":
        blink_led(LED_RIGHT)
    if request.form.get("bottom_led_button") == "bottom_led_button":
        blink_led(LED_BOTTOM)
    return render_template("submit_form.html", form=form)


def blink_led(led):
    GPIO.output(led, GPIO.HIGH)
    sleep(1)
    GPIO.output(led, GPIO.LOW)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
