#!/usr/bin/env python

########################################################################
# Filename    : LED.py
# Description : Provides routines for working with the Grove LED.
# auther      : www.my-pi.xyz
# modification: 2017/03/06
########################################################################

from grovepi import *


def LEDOn(pin):
    # Turns the given pin on
    digitalWrite(pin, 1)


def LEDOff(pin):
    # Turns the given pin off
    digitalWrite(pin, 0)


if __name__ == '__main__':
    print('This is a library, mate...')