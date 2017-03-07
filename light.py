#!/usr/bin/env python

########################################################################
# Filename    : light.py
# Description : Provides functions to work with the Grove light sensor.
# auther      : www.my-pi.xyz
# modification: 2017/03/07
########################################################################

from grovepi import *


def getLightReading(pin):
    # Reads the ligth value from the sensor and returns it plus
    # resistance of sensor in K
    sensor_value = analogRead(pin)
    resistance = (float)(1023 - sensor_value) * 10 / sensor_value

    return sensor_value, resistance

if __name__ == '__main__':
    print('This is a library, mate...')