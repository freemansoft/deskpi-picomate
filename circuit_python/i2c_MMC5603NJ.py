# SPDX-FileCopyrightText: 2025 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# Derived from https://wiki.deskpi.com/picomate/#3-axis-magnetometer
#
# The MMC5603NJ sensor is a 3-axis magnetometer
# The magnetometer values are in microtesla
#
# located at I2C address 0x30
#
# Requires
# adafruit_register
# adafruit_mmc56x3

import time

import adafruit_register
import board
import busio
from adafruit_mmc56x3 import MMC5603

# log the board characteristics
# dir(board)

i2c1 = busio.I2C(scl=board.GP15, sda=board.GP14)

magnetometer = MMC5603(i2c1)
magnetometer.data_rate = 1000
magnetometer.continuous_measurement = True

while True:
    print(magnetometer.magnetic)
    time.sleep(0.1)
