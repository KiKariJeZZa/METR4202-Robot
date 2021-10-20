#! /usr/bin/env python

# ------------------
# Camera functions that get fiducial transforms found on camera
#
# Written by Jeremiah Casuga
# ------------------

import rospy
from fiducial_msgs.msg import FiducialTransformArray
import numpy as np

def callback(data):
    """
    This function will handle all the logic behind
    figuring out which block is of interest

    Returns an array of x y z coordinates
    """
    print("The value of x1: ", data.transforms[0].transform.translation.x)
    #print("The value of x2: ", data.transforms[1].transform.translation.x)
    #print("The value of x3: ", data.transforms[2].transform.translation.x)
    #print("The value of x4: ", data.transforms[3].transform.translation.x)
    x = data.transforms[0].transform.translation.x
    y = data.transforms[0].transform.translation.y
    z = data.transforms[0].transform.translation.z
    return x

def listener():
    """
    Function that initialises a node to constantly read from the fiducial_transforms topic
    """

    rospy.init_node('fiducial_finder')
    #rospy.Subscriber("fiducial_transforms", FiducialTransformArray, callback)
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    print(data.transforms[0].transform.translation.x)


def turntable_move():
    """
    Logic that should return whether the turn table is in motion
    """
    rospy.init_node('fiducial_finder')
    i = 0
    x_array = [0, 0]
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    print(data.transforms[0].transform.translation.x)
    x_array[i] = data.transforms[0].transform.translation.x
    i = 1
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    x_array[i] = data.transforms[0].transform.translation.x
    i = 0

    if abs(x_array[1] - x_array[0]) < 0.0001:
        return False
    else:
        return True
    
def closest_block():
    """
    Logic that returns the closest block to the robot
    """
    return 0

if __name__ == '__main__':
    while 1:
        if turntable_move():
            print("Moving")
        else: 
            print("Not moving")