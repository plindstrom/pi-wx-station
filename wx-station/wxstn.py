# ------------------------------------------------------------------------
# File Name  wxstn.py
# Author     Peter Lindstrom
# Purpose    Record weather data and save to a database.
# Link       https://github.com/plindstrom/pi-wx-station
# Source     https://projects.raspberrypi.org/en/projects/build-your-own-weather-station
# ------------------------------------------------------------------------

import bme280
import mariadb
import math
import smbus2
import time
from gpiozero import Button
from gpiozero import MCP3008

# Interval to record weather data in seconds
interval = 5


# =================================================================== #
# BME280 Configuration                                                #
# =================================================================== #
bme280_enabled = True
bme280_port = 1
bme280_address = 0x77
bme280_altitude_adjust = 179.45
bme280_bus = smbus2.SMBus(bme280_port)
bme280.load_calibration_params(bme280_bus, bme280_address)


# =================================================================== #
# Anemometer Configuration                                            #
# =================================================================== #
speed_enabled = True
speed_radius = 9.0
speed_circumference = (2 * math.pi) * speed_radius
speed_sensor = Button(5)
speed_count = 0


# =================================================================== #
# Wind Vane Configuration                                             #
# =================================================================== #
direction_enabled = True
direction_adc = MCP3008(channel=0)
direction_count = 0
direction_values = []
direction_volts = {
            0.4: 0.0,
            1.4: 22.5,
            1.2: 45.0,
            2.8: 67.5,
            2.7: 90.0,
            2.9: 112.5,
            2.2: 135.0,
            2.5: 157.5,
            1.8: 180.0,
            2.0: 202.5,
            0.7: 225.0,
            0.8: 247.5,
            0.1: 270.0,
            0.3: 292.5,
            0.2: 315.0,
            0.6: 337.5
}


# =================================================================== #
# Rainfall Sensor Configuration                                       #
# =================================================================== #
rainfall_enabled = True
rainfall_bucket_size = 0.2794
rainfall_sensor = Button(6)
rainfall_count = 0


# =================================================================== #
# Read BME280                                                         #
# =================================================================== #
def read_bme280():
    bme280_data = bme280.sample(bme280_bus, bme280_address)
    return bme280_data.temperature, bme280_data.humidity, bme280_data.pressure


# =================================================================== #
# Spin Anemometer                                                     #
# =================================================================== #
def spin_wind():
    global speed_count
    speed_count = speed_count + 1


# =================================================================== #
# Calculate Anemometer Speed                                          #
# =================================================================== #
def calc_wind(read_time):
    global speed_count
    global speed_circumference

    speed_rotations = speed_count / 2.0
    speed_distance = (speed_circumference * speed_rotations) / 100000.0
    speed_return = ((speed_distance / read_time) * 3600) * 1.18

    return speed_return


# =================================================================== #
# Reset Anemometer Speed                                              #
# =================================================================== #
def reset_speed():
    global speed_count
    speed_count = 0


# =================================================================== #
# Calculate Vane Direction                                            #
# =================================================================== #
def calc_direction():
    direction_out = round(direction_adc.value * 3.3, 1)

    if direction_out in direction_volts:
        direction_return = direction_volts[direction_out]
    else:
        direction_return = 999

    return direction_return


# =================================================================== #
# Tip Rainfall Bucket                                                 #
# =================================================================== #
def tip_rainfall():
    global rainfall_count
    rainfall_count = rainfall_count + 1


# =================================================================== #
# Calculate Rainfall Amount                                           #
# =================================================================== #
def calc_rainfall():
    global rainfall_count
    global rainfall_bucket_size
    rainfall_return = rainfall_count * rainfall_bucket_size

    return rainfall_return


# =================================================================== #
# Reset Rainfall Amount                                               #
# =================================================================== #
def reset_rainfall():
    global rainfall_count
    rainfall_count = 0


# =================================================================== #
# Main Program                                                        #
# =================================================================== #
speed_sensor.when_pressed = spin_wind
rainfall_sensor.when_pressed = tip_rainfall

while True:
    reset_speed()
    reset_rainfall()
    time.sleep(interval)

    temperature, humidity, pressure = read_bme280()
    pressure = pressure + bme280_altitude_adjust
    speed = calc_wind(interval)
    direction = calc_direction()
    rainfall = calc_rainfall()

    print("Temperature:    " + str(temperature) + "\nHumidity:       " + str(humidity) + "\nPressure:       " + str(pressure) + "\nWind Speed:     " + str(speed) + "\nWind Direction: " + str(direction) + "\nRainfall:       " + str(rainfall) + "\n")

    wxdb = mariadb.connect(user = "DB_USER_HERE", password = "DB_PASSWORD_HERE", host = "localhost", database = "wx")
    cursor = wxdb.cursor()

    try:
        cursor.execute("INSERT INTO MEASUREMENT (TEMPERATURE, HUMIDITY, PRESSURE, WIND_SPEED, WIND_DIRECTION, RAINFALL) VALUES (?, ?, ?, ?, ?, ?)", (temperature, humidity, pressure, speed, direction, rainfall))
    except mariadb.Error as e:
        print("Error: {e}")

    wxdb.commit()
    wxdb.close()
