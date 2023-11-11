# ------------------------------------------------------------------------
# File Name  rain.py
# Author     Peter Lindstrom
# Purpose    Test the rain sensor; output tip count when bucket tipped.
# Link       https://github.com/plindstrom/pi-wx-station
# Source     https://projects.raspberrypi.org/en/projects/build-your-own-weather-station
# ------------------------------------------------------------------------

from gpiozero import Button

rain_sensor = Button(6)
count = 0

def bucket_tipped():
    global count
    count = count + 1
    print(count)

while True:
    rain_sensor.when_pressed = bucket_tipped
