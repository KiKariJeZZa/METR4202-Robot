#! /usr/bin/env python

# ------------------------------
# Functions that open and close the gripper
# via serial communication with an arduino
#
# Written by Nadia Regli
# ------------------------------

# Import dependenceies
import serial

def open_stepper():
    """
    Function that opens the end effector
    """
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser.flush()

    runStepper = 1
    ser.write(str(runStepper).encode('utf-8'))
    return None


def close_stepper():
    """
    Function that closes the end effector
    """
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser.flush()

    runStepper = 2
    ser.write(str(runStepper).encode('utf-8'))
    return None

#if __name__ == '__main__':
 #   open_stepper()



