# SPDX-FileCopyrightText: 2025 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# I2C device 0x3C is a 128x32 SSD1306 OLED display
#
# Derived from https://wiki.deskpi.com/picomate/#096-128x64-oled-display
#
# Requires
# adafruit_register
# adafruit_framebuf
# adafruit_ssd1306

import time

import board
import busio
from adafruit_ssd1306 import SSD1306_I2C

# log the board characteristics
# dir(board)

i2c0 = busio.I2C(scl=board.GP17, sda=board.GP16)
display = SSD1306_I2C(128, 32, i2c0)


def display_text(str, line):
    # display.fill(0)
    display.text(str, 0, (line % 8) * 8, 1, font_name="font5x8.bin")
    # display.show()


while True:
    display.fill(0)

    display_text("hello World", 0)
    display_text("It's a Deskpi Picomate", 2)

    display.show()

    time.sleep(0.5)
