# SPDX-FileCopyrightText: 2025 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# derived from
# https://wiki.deskpi.com/picomate/#blink-rgb-led
# https://wiki.deskpi.com/picomate/#button

import time

import board
import digitalio
import neopixel

# log the board characteristics
# dir(board)

COLORS = ((50, 0, 0), (0, 50, 0), (0, 0, 50))
# setup to support a string of neopixels but we have just one on this kit
pixels = neopixel.NeoPixel(board.GP22, n=1, brightness=0.4)
# when not pressed button.value is True
# when pressed button.value is False
button = digitalio.DigitalInOut(board.GP26)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    if button.value:
        # print("Button not pressed")
        for i in range(len(pixels)):
            pixels[i] = (0, 0, 0)
    if not button.value:
        # print("button pressed")
        for color in COLORS:
            for i in range(len(pixels)):
                pixels[i] = color
                time.sleep(0.2)
