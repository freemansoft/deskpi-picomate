# SPDX-FileCopyrightText: 2025 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# Must use on device
# Rotary Encoders are implemented using interrupts which are not supported by Blinka/U2IF.
# Derived from https://wiki.deskpi.com/picomate/#rotary-encoder
#
import time

import board
import digitalio
import neopixel
import rotaryio

# log the board characteristics
# dir(board)

COLORS = ((50, 0, 0), (0, 50, 0), (0, 0, 50))
# setup to support a string of neopixels but we have just one on this kit
pixels = neopixel.NeoPixel(board.GP22, n=1, brightness=0.4)

# rotary encoder
encoder = rotaryio.IncrementalEncoder(board.GP7, board.GP6)
last_position = encoder.position
# when not pressed button.value is True
# when pressed button.value is False
swtich = digitalio.DigitalInOut(board.GP26)
swtich.direction = digitalio.Direction.INPUT
swtich.pull = digitalio.Pull.DOWN


while True:
    # This button code DOES not work for me
    if not swtich.value:
        # print("Button not pressed")
        for i in range(len(pixels)):
            pixels[i] = (0, 0, 0)
    if swtich.value:
        # print("button pressed")
        for color in COLORS:
            for i in range(len(pixels)):
                pixels[i] = color
                time.sleep(0.2)
    # turning the encoder cycles the RGB colors
    position = encoder.position
    if last_position is None or last_position != position:
        for color in COLORS:
            for i in range(len(pixels)):
                pixels[i] = color
                time.sleep(0.2)
        last_position = position
