#! /usr/bin/env python

# ------------------
# Camera functions that get fiducial transforms found on camera
#
# Written by Jeremiah Casuga
# ------------------

import rospy
from fiducial_msgs.msg import FiducialTransformArray
import numpy as np
import cv2

def colour_detection():
    """
    Determines which colour the block is and which zone it needs to be dropped at
    """
    return 0

def turntable_move():
    """
    Logic that should return whether the turn table is in motion
    """
    # Just check if one block is moving by comparing their x values
    rospy.init_node('turntable_logic')
    i = 0
    x_array = [0, 0]
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    print(data.transforms[0].transform.translation.y)
    x_array[i] = data.transforms[0].transform.translation.y
    i = 1
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    x_array[i] = data.transforms[0].transform.translation.y
    i = 0
    # Check if error is small enough to see that it has stopped moving
    if abs(x_array[1] - x_array[0]) < 0.0002:
        return False
    else:
        return True
    
def closest_block():
    """
    Logic that returns the closest block to the robot
    """
    #rospy.init_node('closest_block')
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    if len(data.transforms) == 1:
        x_array = [0, 0, 0, 0]
        x_array[0] = data.transforms[0].transform.translation.x
        x_array[1] = data.transforms[1].transform.translation.x
        x_array[2] = data.transforms[2].transform.translation.x
        x_array[3] = data.transforms[3].transform.translation.x
        min_value = min(x_array)
        min_index = x_array.index(min_value)
        
        x = data.transforms[min_index].transform.translation.x
        y = data.transforms[min_index].transform.translation.y
        z = data.transforms[min_index].transform.translation.z
        return x, y, z
        
def get_xyz():
    #rospy.init_node('closest_xyz', anonymous=True)
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    x = data.transforms[0].transform.translation.x
    y = data.transforms[0].transform.translation.y
    z = data.transforms[0].transform.translation.z
    print(x,y,z)
    return x, y, z

if __name__ == '__main__':
    while 1:
        get_xyz()
        #if turntable_move():
            #print("Moving")
        #else: 
            #print("Not moving")
        #print(closest_block())