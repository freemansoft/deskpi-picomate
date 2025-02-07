# SPDX-FileCopyrightText: 2025 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# Logs the PRI sensor value
# 1. Detection is pretty quick, probably 1-2 seconds
# 1. Undetection is about 2-4 seconds
#


import time

import board
import digitalio

# log the board characteristics
# dir(board)

sensor = digitalio.DigitalInOut(board.GP28)
sensor.direction = digitalio.Direction.INPUT
sensor.pull = digitalio.Pull.DOWN

last_value = sensor.value
while True:
    new_value = sensor.value
    if last_value != new_value:
        print("motion " + ("detected!" if new_value else "removed!"))
        last_value = new_value
