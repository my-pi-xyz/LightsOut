#!/usr/bin/env python

########################################################################
# Filename    : display.py
# Description : Provides routines for working with the Grove LCD.
# auther      : www.my-pi.xyz
# modification: 2017/03/06
########################################################################

from grove_rgb_lcd import *


def lcdReset():
    # Clears the text and turns off the backlighting
    lcdClear()
    setRGB(0, 0, 0)


def lcdMonitoring(lapsed):
    # Displays the lapsed time
    lapsedTime = lapsed / 60.00
    outputText = 'Countdown: %05.2f' % lapsedTime

    setRGB(95, 158, 160)
    setText(outputText)


def lcdMonitoringToRedLight(lapsed, toLight):
    # Displays the lapsed time and the time to remaining
    # before the red light goes on
    lapsedTime = lapsed / 60.00
    timeToLight = toLight / 60.00
    outputText = 'Countdown: %05.2f\nLight On : %05.2f' % (lapsedTime, timeToLight)  # lint:ok

    setRGB(95, 158, 160)
    setText(outputText)


def lcdMonitoringToBuzzer(lapsed, toBuzzer):
    # Displays the lapsed time and the time to remaining
    # before the buzzer goes off
    lapsedTime = lapsed / 60.00
    timeToBuzzer = toBuzzer / 60.00
    outputText = 'Countdown: %.2f\nBuzzer   : %.2f' % (lapsedTime, timeToBuzzer)

    setRGB(255, 65, 0)
    setText(outputText)


def lcdClear():
    # Clear the screen by print a blank string
    setText(''.ljust(32))


def putOutLights():
    # Displays the put out lights statement
    setRGB(255, 0, 0)
    setText('Put out lights!')

if __name__ == '__main__':
    print('This is a library, mate...')