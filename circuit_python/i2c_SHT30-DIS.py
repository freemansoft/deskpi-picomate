# SPDX-FileCopyrightText: 2025 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# Derived from https://wiki.deskpi.com/picomate/#temperature-humidity-sensor
#
# The SHT30-DIS sensor is a temperature and humidity sensor
# located at I2C address 0x44
#
# modules and libraries
# afruit_register
# adafruit_lsm6ds

import time

import board
import busio
from adafruit_sht31d import SHT31D

# log the board characteristics
# dir(board)

i2c1 = busio.I2C(board.GP15, board.GP14)
sht_sensor = SHT31D(i2c1)

loopcount = 0

while True:
    print("Temperature: %0.1f C" % sht_sensor.temperature)
    print("Humidity: %0.1f %%" % sht_sensor.relative_humidity)
    loopcount += 1
    time.sleep(2)
    if loopcount == 10:
        loopcount = 0
        sht_sensor.heater = True
        print("Sensor Heater status: %s" % sht_sensor.heater)
        time.sleep(1)
        sht_sensor.heater = True
        print("Sensor Heater status: %s" % sht_sensor.heater)
