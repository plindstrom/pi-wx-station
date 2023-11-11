# ------------------------------------------------------------------------
# File Name  voltage_divider.py
# Author     Peter Lindstrom
# Purpose    Voltage divider for the wind vane.
# Link       https://github.com/plindstrom/pi-wx-station
# Source     https://projects.raspberrypi.org/en/projects/build-your-own-weather-station
# ------------------------------------------------------------------------

resistances = [33000, 6570, 8200, 891, 1000, 688, 2200, 1410, 3900, 3140, 16000, 14120, 120000, 42120, 64900, 21880]

def voltage_divider(r1, r2, vin):
    vout = (vin * r1) / (r1 + r2)
    return round(vout, 3)

for x in range(len(resistances)):
    print(resistances[x], voltage_divider(4700, resistances[x], 3.3))
