# SPDX-FileCopyrightText: 2025 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# Derived from https://wiki.deskpi.com/picomate/#pdm-microphone
#
# prints a version of the volume level
# first: look at the logs idle
# then: speak into the microphone and watch the output
# In Thorny you can plot the output by pressing the `Plotter` button

import array
import math
import time

import audiobusio
import board
import busio

# log the board characteristics
# dir(board)


def mean(values):
    return sum(values) / len(values)


def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * float(sample - minbuf) for sample in values
    )
    return math.sqrt(samples_sum / len(values))


mic = audiobusio.PDMIn(board.GP9, board.GP8, sample_rate=16000, bit_depth=16)

samples = array.array("H", [0] * 160)

while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    print((magnitude,))
    time.sleep(0.1)
