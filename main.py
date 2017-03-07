#!/usr/bin/env python

########################################################################
# Filename    : main.py
# Description : Application entry point.
# auther      : www.my-pi.xyz
# modification: 2017/03/06
########################################################################

from time import sleep
from datetime import *
from grovepi import *
from display import *
from LED import *
from buzzer import *
from motion import *
from clock import RealTimeClock
from light import *

red_LED_pin = 5
buzzer_pin = 6
motion_sensor = 7
real_time_clock = 1
light_sensor = 0


def setup():
    # Initialize the application on startup
    pinMode(red_LED_pin, 'OUTPUT')
    pinMode(buzzer_pin, 'OUTPUT')
    pinMode(motion_sensor, 'INPUT')

    sleep(1)


def destroy():
    # Program clean up
    lcdReset()
    buzzerOff(buzzer_pin)


def loop():
    # Program's main loop
    # myClock = RealTimeClock(real_time_clock)

    sensor_value, resistance = getLightReading(light_sensor)

    print(sensor_value, resistance)

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
