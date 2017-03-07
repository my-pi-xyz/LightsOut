#!/usr/bin/env python

########################################################################
# Filename    : motion.py
# Description : Provides routines for working with the Grove motion sensor.
# auther      : www.my-pi.xyz
# modification: 2017/03/07
########################################################################

from grovepi import *


def isSomeoneThere(pin):
    # Checks if the sensor has detected motion in the room
    if digitalRead(pin):
        return True
    else:
        return False


if __name__ == '__main__':
    print('This is a library, mate...')