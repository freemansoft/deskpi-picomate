# SPDX-FileCopyrightText: 2025 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# Portions of this arederived from https://wiki.deskpi.com/picomate/#digital-optical-sensor
#
# The LTR-381RGB-01 sensor is an optical sensor
# It has a proximity sensor and a color sensor
# located at I2C address 0x53
#
# The library is included in this project and can be found on the Deskpi wiki
#
# Requires
# adafruit_register
# ltr381rgb
#
# I don't see a difference between the ALS and CS modes
#
# mode ALS is a ambient light sensor
# mode CS is a color sensor
#
# Sample CS output
# ALS: 120.756 lx
# (5, 453, 441, 145)
# ALS: 121.014 lx
# (6, 454, 442, 146)
#
# Sample ALS output
# ALS: 111.689 lx
# (5, 419, 413, 132)
# ALS: 112.48 lx
# (6, 422, 415, 132)


import time

import board
import busio
from ltr381rgb import LTR381RGB

i2c1 = busio.I2C(scl=board.GP15, sda=board.GP14)

# Optical Sensor
optical = LTR381RGB(i2c1)
optical.mode = "ALS"
optical.enable()

# ALS and raw data plotter
while True:
    print(f"ALS: {optical.lux} lx")
    print(optical.raw_data)
    time.sleep(0.5)
