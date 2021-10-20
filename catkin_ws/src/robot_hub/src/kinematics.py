#! /usr/bin/env python

# ------------------------------------------
# Kinematics hub for the logic behind the robot
#
# Written by Jeremiah Casuga
# Assisted by Nadia Regli
# ------------------------------------------

import modern_robotics as mr
import numpy as np
import rospy

def end_effector_pos(M, Slist, thetalist):
    """
    Returns the forward kinematics of the end effector in space
    """
    return FKinSpace(M, Slist, thetalist)

def desired_angle_config(Slist, M, thetalist):
    """
    Returns an array of desired joint configurations for the robot to move to
    """
    # Set initial error tolerances
    eomg = 0.001
    ev = 0.001
    for i in range(220, 280):
        theta = i * np.pi / 180
        # T will be arbitrary for now
        T = np.array([[np.cos(theta), -np.sin(theta), 0, 0.10],
                    [np.sin(theta), np.cos(theta), 0, -0.01],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])   
        outcome = mr.IKinSpace(Slist, M, T, thetalist, eomg, ev)
        joint1 = np.degrees(outcome[0][0])
        joint2 = np.degrees(outcome[0][1])
        joint3 = np.degrees(outcome[0][2])
        joint4 = np.degrees(outcome[0][3])
        if outcome[1] == True:
            if -90 <= joint1 <= 90:
                if -90 <= joint2 <= 90:
                    if -90 <= joint3 <= 90:
                        joint1 = joint1 * np.pi / 180
                        joint2 = joint2 * np.pi / 180
                        joint3 = joint3 * np.pi / 180
                        joint4 = joint4 * np.pi / 180
                        if -0.0001 <= joint1 <= 0.0001:
                            joint1 = 0
                        if -0.0001 <= joint2 <= 0.0001:
                            joint2 = 0
                        if -0.0001 <= joint3 <= 0.0001:
                            joint3 = 0
                        if -0.0001 <= joint4 <= 0.0001:
                            joint4 = 0
                        print(f'Joint1 Angle: {joint1}, Joint2 Angle: {joint2}, Joint3 Angle: {joint3}, Joint4 Angle: {joint4}')
                        return np.array([joint1, joint2, joint3, joint4])
                        break
        else:
            print("No solution found")
            