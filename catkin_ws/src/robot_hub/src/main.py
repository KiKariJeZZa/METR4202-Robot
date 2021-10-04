#! /usr/bin/env python

# ------------------------------------------
# Main hub for the logic behind the robot
#
# Written by Jeremiah Casuga
# ------------------------------------------

# Firstly import dependancies
import rospy
import modern_robotics as mr
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import numpy as np

def move_servo(des_pos):
    """Function that takes desired joint state information and publishes
    to the topic  

    :param des_pos: Desired joint angles list
    :return: none
    """
    rospy.init_node('main_loop')
    servo_publisher = rospy.Publisher('/desired_joint_states', JointState, queue_size = 10)
    rate = rospy.Rate(10) # 10hz
    # Build the required string needed to send to the topic
    state_str = JointState()
    state_str.header = Header()
    state_str.header.stamp = rospy.Time.now()
    state_str.name = ['joint_1','joint_2','joint_3','joint_4']
    state_str.position = [des_pos[0],des_pos[1],des_pos[2],des_pos[3]]
    state_str.velocity = [0.5,0.5,0.5,0.5]
    state_str.effort = []
    while not rospy.is_shutdown():
        state_str.header.stamp = rospy.Time.now()
        # Send to topic
        servo_publisher.publish(state_str)
        #print("Message successfully published")
        rate.sleep()
        if JointState().position == state_str.position :
            print(state_str)
            rospy.shutDown()

def zero_position():
    """ Function that returns the robot configuration to its zero position

    :param: none
    :return: array of zero position
    """
    return np.array([0,1.5,0,0])

if __name__ == '__main__':
    move_servo(zero_position())
    