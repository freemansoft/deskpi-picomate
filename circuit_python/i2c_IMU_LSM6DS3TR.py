# SPDX-FileCopyrightText: 2025 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# Code derived from https://wiki.deskpi.com/picomate/#6-axis-imu-sensor
#
# The output of this program is the acceleration and gyroscope values from the LSM6DS3TRC sensor
# The output can be plotted in the output view in thorny
#
# The LSM6DS3TRC sensor is a 3-axis accelerometer and 3-axis gyroscope
# The accelerometer values are in m/s^2
# located at I2C address 0x6A
#
# Requires
# dafruit_register
# adafruit_lsm6ds

import time

import adafruit_register
import board
import busio
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

# log the board characteristics
# dir(board)

i2c1 = busio.I2C(scl=board.GP15, sda=board.GP14)

imu_sensor = LSM6DS3TRC(i2c1)

# Can't add any debug out put because that will break plot data stream

# Accelleration
while True:
    print(imu_sensor.acceleration)
    time.sleep(0.1)

# Gyroscope
while True:
    print(imu_sensor.gyro)
    time.sleep(0.1)
