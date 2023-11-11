# ------------------------------------------------------------------------
# File Name  cleanup.py
# Author     Peter Lindstrom
# Purpose    Summarize and remove old data from the database.
# Link       https://github.com/plindstrom/pi-wx-station
# Source     https://projects.raspberrypi.org/en/projects/build-your-own-weather-station
# ------------------------------------------------------------------------

import mariadb
from datetime import datetime, timedelta

selectdate = datetime.now() - timedelta(days = 30)
print("Cleaning up records older than " + selectdate.strftime("%Y-%m-%d %H:59:59") + ".")

wxdb = mariadb.connect(user = "DB_USER_HERE", password = "DB_PASSWORD_HERE", host = "localhost", database = "wx")
cursor = wxdb.cursor()

try:
    cursor.execute("SELECT AVG(TEMPERATURE) AS AVG_TEMPERATURE, AVG(HUMIDITY) AS AVG_HUMIDITY, AVG(PRESSURE) AS AVG_PRESSURE, AVG(WIND_SPEED) AS AVG_WIND, MAX(WIND_SPEED) AS MAX_WIND, AVG(WIND_DIRECTION) AS AVG_WIND_DIRECTION, SUM(RAINFALL) AS SUM_RAINFALL, RECORDED FROM MEASUREMENT WHERE RECORDED BETWEEN '2020-01-01' AND '" + selectdate.strftime("%Y-%m-%d %H:59:59") + "' GROUP BY HOUR(RECORDED), DAY(RECORDED) ORDER BY ID DESC")
    results = cursor.fetchall()
except mariadb.Error as e:
    print("Error: {e}")

for AVG_TEMPERATURE, AVG_HUMIDITY, AVG_PRESSURE, AVG_WIND, MAX_WIND, AVG_WIND_DIRECTION, SUM_RAINFALL, RECORDED in results:
    print(f"{RECORDED} - TEMP: {AVG_TEMPERATURE}, HUMID: {AVG_HUMIDITY}, PRESUR: {AVG_PRESSURE}, WIND: {AVG_WIND}, MWIND: {MAX_WIND}, WDIR: {AVG_WIND_DIRECTION}, RAIN: {SUM_RAINFALL}")
    try:
        cursor.execute("INSERT INTO LTR_MEASUREMENT (AVG_TEMPERATURE, AVG_HUMIDITY, AVG_PRESSURE, AVG_WIND, MAX_WIND, AVG_WIND_DIRECTION, SUM_RAINFALL, RECORDED) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (AVG_TEMPERATURE, AVG_HUMIDITY, AVG_PRESSURE, AVG_WIND, MAX_WIND, AVG_WIND_DIRECTION, SUM_RAINFALL, RECORDED))
        wxdb.commit()
    except mariadb.Error as e:
        print("Error: {e}")

try:
    cursor.execute("DELETE FROM MEASUREMENT WHERE RECORDED BETWEEN '2020-01-01' AND '" + selectdate.strftime("%Y-%m-%d %H:59:59") + "'")
except mariadb.Error as e:
    print("Error: {e}")

wxdb.commit()
wxdb.close()
