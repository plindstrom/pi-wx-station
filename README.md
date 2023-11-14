# pi-wx-station
![Built with Python](https://img.shields.io/badge/Built_with-Python-blue?logo=python)
![CC BY SA 4.0 Deed License](https://img.shields.io/badge/license-CC_BY_SA_4.0_Deed-orange)


This repository contains the scripts used to gather weather data on a Raspberry Pi, store the data in a database, and display the weather data on a locally hosted web site.

Everything here is based on the original Raspberry Pi project [Build Your Own Weather Station](https://projects.raspberrypi.org/en/projects/build-your-own-weather-station).  The project is also available on GitHub: https://github.com/raspberrypilearning/build-your-own-weather-station.  I recommend using the original documentation for more comprehensive information on how to build the weather station, plus I did not include all the sensors that are included in the original project (ground temperature and air quality).

## Supplies
I purchased the following equipment for an outdoor headless weather station, and an indoor weather display station (which also has a BME280 to read inside temperature and humidity).  Everything was purchased in 2020, so availability and prices have likely changed.

| Part | Qty | Price |
| ---- | --- | ----- |
| Raspberry Pi 4 Model B 4GB | 2 | $49.99 |
| Raspberry Pi Power supply | 2 | $7.99 |
| Micro HDMI cable | 1 | $9.98 |
| 32GB microSD Card w/ Adapter | 2 | $12.99 |
| Adafruit BME280 - Humidity, Pressure, Temperature Sensor | 2 | $19.95 |
| SK-28 Enclosure with Knockouts | 1 | $33.36 |
| SK-11 Enclosure with Knockouts | 1 | $9.18 |
| Vent Plug | 1 | $3.44 |
| Inland 400 Tie-Point Breadboard | 1 |  |
| Inland 30CM 40-PIN F-F Jumper Wire | 1 |  |
| Inland 30CM 40-PIN F-M Jumper Wire | 1 |  |
| SparkFun Weather Meter Kit SEN-15901 | 1 | $69.95 |
| SparkFun RJ11 Breakout BOB-14021 | 1 | $1.95 |

## Connecting the Sensors
![Diagram of Sensor Connections](https://github.com/plindstrom/pi-wx-station/blob/main/docs/Connections.svg)

After the sensors are connected as shown above, you can test the individual sensors to make sure everything is working as expected using some simple test scripts.

## Test the BME280
The BME280 measures humidity, pressure and temperature.  It requires an additional Python library which will need to be installed before testing.

Download the Raspberry Pi Foundation weather station data logging code:
```
git clone https://github.com/RaspberryPiFoundation/weather-station
```

Install the BME280 Python library:
```
sudo pip3 install RPi.bme280
```

If you have trouble (I was getting a 403 error running the above command), try downloading the library from https://pypi.org/project/RPi.bme280/#files and then run:
```
sudo pip3 install /home/pi/Downloads/RPi.bme280-0.2.3.tar.gz
```

Enable I2C in the Raspberry Pi settings under Preferences > Raspberry Pi Configuration > Interfaces.

To verify the BM280 is working, try running the bme280.py script.  If everything is working, you should see the current humidity, pressure (Pascal) and temperature (Celsius) print to the screen every second.  Try blowing on the sensor and you should observe the humidity and temperature increase (line six in the example below).
```
29.208259738398066 838.3659517344039 81.38188475355972
29.19013874739269 838.3465987400685 81.39106836495107
29.196424959721586 838.3324319390911 81.37270114269224
29.184147518025313 838.3465987400685 81.39106836495107
29.207817609114194 838.3607656407214 81.40943558930536
65.51933144936166 838.3715738315233 82.65841176138376
81.31459543145212 838.4040186863983 84.24719692368527
83.51837637557152 838.4165863776927 84.64209971479256
81.60270533611725 838.4384593568121 83.46657797715744
81.51929154803435 838.4198892899261 82.96147361688782
78.98633723539038 838.4371867924331 82.12575897359406
76.25058854012028 838.4315628259551 82.01555516855908
70.3300637195136 838.4371867924331 82.12575897359406
48.85122094738878 838.4532217477823 82.18086090440048
41.07286029584125 838.4111294431807 82.26351383597125
37.508814372497675 838.4305050274971 82.25433017481235
35.93518804018035 838.4021810930983 82.21759553541546
34.325142242024434 838.4196857468722 82.1716772479564
33.720684009815166 838.3913609846862 82.13494262741878
32.86460112072621 838.3630366186414 82.09820801526308
33.24824900344773 838.3682457746796 82.07065706164693
32.5836055068511 838.4334387862685 82.05228976185549
32.00297181732664 838.4051118747742 82.01555516855908
31.517549595635394 838.3592912856651 82.02473881609738
31.05066103078725 838.3309663901745 81.98800422908738
30.877134964983426 838.3697037930796 81.9696369387256
```

### Test the Anemometer
The Aneometer counts the number of spins it completes in a given time to calculate the wind speed.

To verify the Aneometer is working, try running the wind.py script.  If everything is working, you should see the spin count and calculated speed print to the screen every five seconds.  Try spinning the aneometer at different speeds and watch as the output changes.
