#! /usr/bin/env python

# ------------------
# Camera functions that get fiducial transforms found on camera
#
# Written by Jeremiah Casuga
# ------------------

# Import dependencies
import rospy
from fiducial_msgs.msg import FiducialTransformArray
from sensor_msgs.msg import Image
import numpy as np
import cv2
from color_detector import ColorDetector
from numpy.core.fromnumeric import argmin, argmax
from ximea import xiapi

def turntable_move():
    """
    Logic that should return whether the turn table is in motion
    """
    # Just check if one block is moving by comparing their x values
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    # Ensure at least one fiducial is being read
    if len(data.transforms) >= 1:
        x_array = [0, 0]
        i = 0
        x_array[i] = data.transforms[0].transform.translation.y
        if len(data.transforms) >= 1:
            i = 1
            data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
            try:
                x_array[i] = data.transforms[0].transform.translation.y
            except IndexError:
                pass
            i = 0
            
        else:
            return True
        # Check if error is small enough to see that it has stopped moving
        if abs(x_array[1] - x_array[0]) < 0.0002:
            return False
        else:
            return True 
    else:
        return True
    
def closest_block():
    """
    Logic that returns the closest block to the robot
    """
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    if len(data.transforms) >= 1:
        # Store an array and check the closest to the robot
        for i in range(len(data.transforms)):
            x_array = [0 for i in range(len(data.transforms))]
            x_array[i] = data.transforms[i].transform.translation.y
        max_value = max(x_array)
        max_index = x_array.index(max_value)
        print(max_index)
        x = data.transforms[max_index].transform.translation.x
        y = data.transforms[max_index].transform.translation.y
        z = data.transforms[max_index].transform.translation.z
        x_q = data.transforms[max_index].transform.rotation.x
        y_q = data.transforms[max_index].transform.rotation.y
        z_q = data.transforms[max_index].transform.rotation.z
        w_q = data.transforms[max_index].transform.rotation.w
        return x, y, z, x_q, y_q, z_q, w_q
        
def get_xyz():
    """
    Function that returns x y z coordinates of fiducial marker
    Mainly used to calibrate where robot is compared to camera
    """
    #rospy.init_node('closest_xyz', anonymous=True)
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    if len(data.transforms) >= 1:
        print("Detecting fiducials")
        x = data.transforms[0].transform.translation.x
        y = data.transforms[0].transform.translation.y
        z = data.transforms[0].transform.translation.z
        print(x,y,z)
        return x, y, z
    

if __name__ == '__main__':
    while 1:
        #x,y,z = get_xyz()
        get_xyz()
        #if turntable_move():
            #print("Moving")
        #else: 
            #print("Not moving")
        #print(closest_block())