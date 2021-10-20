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
import kinematics as k
import stepper as step
import camera as cam

# Declare variables for the robot
joint2_offset = 1.5
M = np.array([[1, 0, 0, 0.0565],
            [0, 1, 0, 0.205],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])
Slist = np.array([[0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0.03, 0, 0],
                [0, 0, 1, 0.12, 0, 0],
                [1, 0, 0, 0, 0, -0.205]]).T
thetalist = np.array([0, 0, 0, 0])

def move_servo(des_pos):
    """
    Function that takes desired joint state information and publishes
    to the topic  
    """
    rospy.init_node('main_loop')
    servo_publisher = rospy.Publisher('/desired_joint_states', JointState, queue_size = 10)
    rate = rospy.Rate(10) # 10hz
    # Build the required string needed to send to the topic
    state_str = JointState()
    state_str.header = Header()
    state_str.header.stamp = rospy.Time.now()
    state_str.name = ['joint_1','joint_2','joint_3','joint_4']
    state_str.position = [des_pos[0],des_pos[1]+joint2_offset,des_pos[2],des_pos[3]]
    state_str.velocity = [1.25,0.75,1,1]
    state_str.effort = []
    count = 0
    print("Moving to desired position")
    while count < 50:
        state_str.header.stamp = rospy.Time.now()
        # Send to topic
        servo_publisher.publish(state_str)
        #print("Message successfully published")
        rate.sleep()
        count = count + 1
        

def zero_position():
    """ 
    Function that returns the robot configuration to its zero position
    """
    print("Moving to zero position")
    return np.array([0, 0, 0, 0])

def zone_dropoff():
    """
    Function that returns the robot configuration for each drop off zone
    """
    Zone1 = np.array([1.8, -1, -0.8, 0])
    Zone2 = np.array([-0.35, 1, 2, 0])
    Zone3 = np.array([0.35, 1, 2, 0])
    Zone4 = np.array([-1.8, -1, -0.8, 0])
    return Zone3




# ---------
# Servo Limits
# Joint1: +- 2.6
# Joint2: -1.35
# Joint3: -1.487
# Joint4: No limits
# ---------

if __name__ == '__main__':
    #move_servo(k.desired_angle_config(Slist, M, thetalist))
    #move_servo(zero_position())
    #move_servo(zone_dropoff())
    #move_servo(zero_position())
    print(cam.listener())
    