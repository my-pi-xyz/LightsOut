#!/usr/bin/env python

########################################################################
# Filename    : clock.py
# Description : Provides routines for working with the Grove RTC.
# auther      : www.my-pi.xyz
# modification: 2017/03/07
########################################################################

import datetime
import smbus


class RealTimeClock():
    # Wraps the Grove RTC for easy use

    def __init__(self, pin):
        # Initializes the RTC
        self.MON = 1
        self.TUE = 2
        self.WED = 3
        self.THU = 4
        self.FRI = 5
        self.SAT = 6
        self.SUN = 7
        self.DS1307_I2C_ADDRESS = 0x68
        self.bus = smbus.SMBus(pin)

        # Set the current values
        current = datetime.datetime.now()
        self.fillByYMD(current.year, current.month, current.day)
        self.fillByHMS(current.hour, current.minute, current.second)
        self.fillDayOfWeek(current.weekday() + 1)
        self.setTime()

    def decToBcd(self, val):
        return ((val / 10 * 16) + (val % 10))

    def bcdToDec(self, val):
        return ((val / 16 * 10) + (val % 16))

    def setTime(self):
        data = [self.decToBcd(self.second), self.decToBcd(self.minute),
            self.decToBcd(self.hour), self.decToBcd(self.dayOfWeek),
            self.decToBcd(self.dayOfMonth), self.decToBcd(self.month),
            self.decToBcd(self.year)]

        self.bus.write_byte(self.DS1307_I2C_ADDRESS, 0x00)
        self.bus.write_i2c_block_data(self.DS1307_I2C_ADDRESS, 0x00, data)

    def getTime(self):
        self.bus.write_byte(self.DS1307_I2C_ADDRESS, 0x00)
        data = self.bus.read_i2c_block_data(self.DS1307_I2C_ADDRESS, 0x00)
        #A few of these need masks because certain bits are control bits
        self.second = self.bcdToDec(data[0] & 0x7f)
        self.minute = self.bcdToDec(data[1])
        self.hour = self.bcdToDec(data[2] & 0x3f)
        self.dayOfWeek = self.bcdToDec(data[3])
        self.dayOfMonth = self.bcdToDec(data[4])
        self.month = self.bcdToDec(data[5])
        self.year = self.bcdToDec(data[6])

    def fillByHMS(self, _hour, _minute, _second):
        self.hour = _hour
        self.minute = _minute
        self.second = _second

    def fillByYMD(self, _year, _month, _day):
        self.year = _year - 2000
        self.month = _month
        self.dayOfMonth = _day

    def fillDayOfWeek(self, _dow):
        self.dayOfWeek = _dow


if __name__ == '__main__':
    print('This is a library, mate...')