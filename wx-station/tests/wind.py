# ------------------------------------------------------------------------
# File Name  wind.py
# Author     Peter Lindstrom
# Purpose    Test the anemometer; output data every five seconds.
# Link       https://github.com/plindstrom/pi-wx-station
# Source     https://projects.raspberrypi.org/en/projects/build-your-own-weather-station
# ------------------------------------------------------------------------

import math
import statistics
import time
from gpiozero import Button

wind_count = 0
wind_interval = 5
radius_cm = 9.0
store_speeds = []

def spin():
    global wind_count
    wind_count = wind_count + 1
    print("Count: ", wind_count)

def calc_speed(time_sec):
    global wind_count
    circumference_cm = (2 * math.pi) * radius_cm
    rotations = wind_count / 2.0

    dist_km = (circumference_cm * rotations) / 100000.0
    speed = ((dist_km / time_sec) * 3600) * 1.18

    return speed

def reset_wind():
    global wind_count
    wind_count = 0

wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin

while True:
    reset_wind()
    time.sleep(wind_interval)
    print("Wind Speed:", calc_speed(wind_interval), "km/h")
