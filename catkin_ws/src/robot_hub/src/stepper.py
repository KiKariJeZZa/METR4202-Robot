#! /usr/bin/env python

import serial


def open_stepper():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser.flush()

    runStepper = 1
    ser.write(str(runStepper).encode('utf-8'))
    return None


def close_stepper():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser.flush()

    runStepper = 2
    ser.write(str(runStepper).encode('utf-8'))
    return None

#if __name__ == '__main__':
 #   open_stepper()



