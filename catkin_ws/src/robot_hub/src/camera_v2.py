#! /usr/bin/env python

# ------------------
# Camera functions that get fiducial transforms found on camera
#
# Written by Jeremiah Casuga
# ------------------

import rospy
from fiducial_msgs.msg import FiducialTransformArray
from sensor_msgs.msg import Image
import numpy as np
import cv2
from color_detector import ColorDetector
from numpy.core.fromnumeric import argmin, argmax
from ximea import xiapi


def colour_detection(x, y):
    """
    Determines which colour the block is and which zone it needs to be dropped at
    """
    print("I am running")
    bgr_r = np.array([0, 0, 255]).astype(np.uint8)
    bgr_g = np.array([0, 255, 0]).astype(np.uint8)
    bgr_b = np.array([255, 0, 0]).astype(np.uint8)
    bgr_y = np.array([0, 255, 255]).astype(np.uint8)
    color_detector = ColorDetector(bgr_r, bgr_g, bgr_b, bgr_y)
    data = rospy.wait_for_message("ximea_cam/image_raw", Image)
    print("I am here now")
    bgr = data.data[y, x, :].astype(np.uint8)
    print("Detected " + ["red", "green", "blue", "yellow", "white", "black"][color_detector.detect_color(bgr)])

def turntable_move():
    """
    Logic that should return whether the turn table is in motion
    """
    # Just check if one block is moving by comparing their x values
    rospy.init_node('turntable_logic')
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    if len(data.transforms) >= 1:
        x_array = [0, 0]
        i = 0
        #print(data.transforms[0].transform.translation.y)
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
    else:
        return True
    
def closest_block():
    """
    Logic that returns the closest block to the robot
    """
    #rospy.init_node('closest_block')
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    if len(data.transforms) >= 1:
        for i in range(len(data.transforms)):
            x_array = [0 for i in range(len(data.transforms))]
            x_array[i] = data.transforms[i].transform.translation.x
        min_value = min(x_array)
        min_index = x_array.index(min_value)
        print(min_index)
        x = data.transforms[min_index].transform.translation.x
        y = data.transforms[min_index].transform.translation.y
        z = data.transforms[min_index].transform.translation.z
        return x, y, z
        
def get_xyz():
    rospy.init_node('closest_xyz', anonymous=True)
    data = rospy.wait_for_message("fiducial_transforms", FiducialTransformArray)
    if len(data.transforms) >= 1:
        print("Detecting fiducials")
        x = data.transforms[0].transform.translation.x
        y = data.transforms[0].transform.translation.y
        z = data.transforms[0].transform.translation.z
        tag = data.transforms[0].fiducial_id
        print(x,y,z,tag)
        return x, y, z, tag

def get_colour_pos():
    data = rospy.wait_for_message("fiducial_vertices", FiducialArray)
    if len(data.transforms) >=1:
        print("Detecting colour position")
        tag_id = get_xyz(3)
        x0 = data.fiducials[tag_id].x0
        y0 = data.ficudials[tag_id].y0
        x3 = data.fiducials[tag_id].x3
        y3 = data.fiducials[tag_id].y3
        x_c = x0 + 0.0001*(x0 - x3)
        y_c = y0 + 0.0001*(y0 - y3)
        return x_c, y_c
    

if __name__ == '__main__':
    while 1:
        #x,y,z = get_xyz()
        get_xyz()
        #if turntable_move():
            #print("Moving")
        #else: 
            #print("Not moving")
        #closest_block()
