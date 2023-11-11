# ------------------------------------------------------------------------
# File Name  bme280.py
# Author     Peter Lindstrom
# Purpose    Test the BME280 sensor; output data every second.
# Link       https://github.com/plindstrom/pi-wx-station
# Source     https://projects.raspberrypi.org/en/projects/build-your-own-weather-station
# ------------------------------------------------------------------------

import bme280
import smbus2
from time import sleep

# Set address depending on the sensor (generally it will be 0x76 or 0x77)
port = 1
address = 0x77
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

# Read data from the sensor every second
while True:
    bme280_data = bme280.sample(bus, address)
    humidity = bme280_data.humidity
    pressure = bme280_data.pressure
    temperature = bme280_data.temperature
    print(humidity, pressure, temperature)
    sleep(1)
