# SPDX-FileCopyrightText: 2025 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#


import time

import board
import neopixel

# log the board characteristics
# dir(board)

COLORS = ((50, 0, 0), (0, 50, 0), (0, 0, 50))
pixels = neopixel.NeoPixel(board.GP22, n=1, brightness=0.4)

while True:
    for cycle in range(2):
        for color in COLORS:
            for i in range(len(pixels)):
                pixels[i] = color
                time.sleep(0.2)
    pixels[i] = (0, 0, 0)
    time.sleep(1)
