#! /usr/bin/env python

# ------------------
# Camera functions that get fiducial transforms found on camera
#
# Written by Jeremiah Casuga
# ------------------

import rospy
from fiducial_msgs.msg import FiducialTransformArray

def callback(data):
    print("The value of x: ", data.transforms[0].transform.translation.x)

def listener():
    print("Initialising")
    rospy.init_node('fiducial_finder')
    print("Initialising2")
    rospy.Subscriber("fiducial_transforms", FiducialTransformArray, callback)
    rospy.spin()

if __name__ == '__main__':
    
    listener()