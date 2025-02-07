# SPDX-FileCopyrightText: 2025 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# Derived from https://wiki.deskpi.com/picomate/#buzzer

import time

import board
import digitalio
import pwmio

# log the board characteristics
# dir(board)

# Auto formatter made these all one per line :-()
TONE_FREQ = [
    1047,
    1047,
    1568,
    1568,
    1760,
    1760,
    1568,
    0,
    1397,
    1397,
    1319,
    1319,
    1175,
    1175,
    1047,
    0,
    1568,
    1568,
    1397,
    1397,
    1319,
    1319,
    1175,
    0,
    1568,
    1568,
    1397,
    1397,
    1319,
    1319,
    1175,
    0,
    1047,
    1047,
    1568,
    1568,
    1760,
    1760,
    1568,
    0,
    1397,
    1397,
    1319,
    1319,
    1175,
    1175,
    1047,
    0,
]

buzzer = pwmio.PWMOut(board.GP27, variable_frequency=True)
# This cant start with a frequency of 0 so we start with 1
buzzer.frequency = 1
buzzer.duty_cycle = 32768

# when not pressed button.value is True
# when pressed button.value is False
button = digitalio.DigitalInOut(board.GP26)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP


while True:
    if not button.value:
        # print("button pressed")
        for note in TONE_FREQ:
            print(note)
            if note:
                buzzer.frequency = note
            time.sleep(0.1)
    # pretty much silent
    buzzer.frequency = 1
