#! /usr/bin/env python

import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser.flush()

    runStepper = 1
    ser.write(str(runStepper).encode('utf-8'))
