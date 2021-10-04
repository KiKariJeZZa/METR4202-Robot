#! /usr/bin/env python

# ------------------------------------------
# Main hub for the logic behind the robot
#
# Written by Jeremiah Casuga
# ------------------------------------------

import rospy
import modern_robotics as mr
from sensor_msgs.msg import JointState


def move_servo():
    """Function that takes desired joint state information and publishes
    to the topic  

    :param states: Desired joint angles
    :return: none
    """
    rospy.init_node('main_loop')
    servo_publisher = rospy.Publisher('desired_joint_states', JointState, queue_size = 1)

    servo_publisher.publish([], ['joint_1'], [1], [0.5], [])
    print("Message successfully published")
    rospy.spin()

if __name__ == '__main__':
    move_servo()
    