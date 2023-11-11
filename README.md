# pi-wx-station
![Built with Python](https://img.shields.io/badge/Built_with-Python-blue?logo=python)
![CC BY SA 4.0 Deed License](https://img.shields.io/badge/license-CC_BY_SA_4.0_Deed-orange)


This repository contains the scripts used to gather weather data on a Raspberry Pi, store the data in a database, and display the weather data on a locally hosted web site.

Everything is based on the original Raspberry Pi project [Build Your Own Weather Station](https://projects.raspberrypi.org/en/projects/build-your-own-weather-station).  The original project is also available on GitHub: https://github.com/raspberrypilearning/build-your-own-weather-station).

## Supplies
I purchased the following equipment for the weather station.  This was purchased in 2020, so availability and prices have likely changed.

| Part | Price |
| ---- | ----- |
| Raspberry Pi 4 Model B 4GB | $49.99 |
| Raspberry Pi Power supply | $7.99 |
| Micro HDMI cable | $9.98 |
| 32GB microSD Card w/ Adapter | $12.99 |
| Adafruit BME280 - Humidity, Pressure, Temperature Sensor | $19.95 |
| SK-28 Enclosure with Knockouts | $33.36 |
| SK-11 Enclosure with Knockouts | $9.18 |
| Vent Plug | $3.44 |
| Inland 400 Tie-Point Breadboard |  |
| Inland 30CM 40-PIN F-F Jumper Wire |  |
| Inland 30CM 40-PIN F-M Jumper Wire |  |
| SparkFun Weather Meter Kit SEN-15901 | $69.95 |
| SparkFun RJ11 Breakout BOB-14021 | $1.95 |

## Connecting the Sensors
![Diagram of Sensor Connections](https://github.com/plindstrom/pi-wx-station/blob/main/docs/Connections.svg)

## Setup the BME280
Download the Raspberry Pi Foundation weather station data logging code:
```
git clone https://github.com/RaspberryPiFoundation/weather-station
```

Install the BME280 Python library:
```
sudo pip3 install RPi.bme280
```

If you have trouble (I was getting a 403 error), try downloading the library from https://pypi.org/project/RPi.bme280/#files and then execute:
```
sudo pip3 install /home/pi/Downloads/RPi.bme280-0.2.3.tar.gz
```

Enable I2C in the Raspberry Pi settings.

