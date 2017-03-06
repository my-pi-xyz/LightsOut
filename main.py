#!/usr/bin/env python

########################################################################
# Filename    : main.py
# Description : Application entry point.
# auther      : www.my-pi.xyz
# modification: 2017/03/06
########################################################################

from time import sleep
from grovepi import *
from display import *
from LED import *
from buzzer import *


red_LED_pin = 5
buzzer_pin = 6


def setup():
    # Initialize the application on startup
    pinMode(red_LED_pin, 'OUTPUT')
    pinMode(buzzer_pin, 'OUTPUT')

    sleep(1)


def destroy():
    # Program clean up
    lcdReset()


def loop():
    while True:
        buzzerOn(buzzer_pin)
        sleep(1)
        buzzerOff(buzzer_pin)
        sleep(1)

    # Program main loop

    destroy()


# -----------------------------------------------------------------------
# Program Start
# -----------------------------------------------------------------------


if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        # When 'Ctrl+C' is pressed we need to clean up and exit.
        destroy()
