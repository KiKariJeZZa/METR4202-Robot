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

def move_servo():
    """Function that takes desired joint state information and publishes
    to the topic  

    :param states: Desired joint angles
    :return: none
    """
    rospy.init_node('main_loop')
    servo_publisher = rospy.Publisher('desired_joint_states', JointState, queue_size = 10)
    rate = rospy.Rate(10) # 10hz
    # Build the required string needed to send to the topic
    state_str = JointState()
    state_str.header = Header()
    state_str.header.stamp = rospy.Time.now()
    state_str.name = ['joint_1','joint_2','joint_3','joint_4']
    state_str.position = [0,1.5,0,0]
    state_str.velocity = [0.5,0.5,0.5,0.5]
    state_str.effort = []
    while not rospy.is_shutdown():
        state_str.header.stamp = rospy.Time.now()
        # Send to topic
        servo_publisher.publish(state_str)
        print("Message successfully published")
        rate.sleep()

if __name__ == '__main__':
    move_servo()
    