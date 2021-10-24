#! /usr/bin/env python

# ------------------------------------------
# Kinematics hub for the logic behind the robot
#
# Written by Jeremiah Casuga
# Assisted by Nadia Regli
# ------------------------------------------

# Import dependencies
import modern_robotics as mr
import numpy as np
import rospy
import camera as cam
from scipy.spatial.transform import Rotation as R

# Declare robot variables
T0_1 = np.array([[1, 0, 0, 0.147],
            [0, 1, 0, 1.01], #0.88 for demo
            [0, 0, 1, 0],
            [0, 0, 0, 1]])
M = np.array([[1, 0, 0, 0.09],
            [0, 1, 0, 0.205],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])
Slist = np.array([[0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0.03, 0, 0],
                [0, 0, 1, 0.12, 0, 0],
                [1, 0, 0, 0, 0, -0.205]]).T
thetalist = np.array([0, 0, 0, 0])

def block_transformation(x, y, z):
    """
    Function that returns the transformation matrix from the camera
    to the block
    """
    T1_2 = np.array([[1, 0, 0, -y],
            [0, 1, 0, -z],
            [0, 0, 1, x], #-x
            [0, 0, 0, 1]])
    print(np.dot(T0_1,T1_2))
    return np.dot(T0_1,T1_2)
    

def end_effector_pos(M, Slist, thetalist):
    """
    Returns the forward kinematics of the end effector in space
    """
    return FKinSpace(M, Slist, thetalist)

def newton_raphson(min_ang, max_ang, array, ee_rotation):
    """
    Function that finds the desired angle configuration of the end effector
    to pick up the block
    """
    # Set initial error tolerances
    eomg = 0.005
    ev = 0.005
    # T will be arbitrary for now
    for i in range(min_ang, max_ang):
        theta = i * np.pi / 180
        T = np.array([[np.cos(theta), -np.sin(theta), 0, array[0][3]],
                    [np.sin(theta), np.cos(theta), 0, array[1][3]],
                    [0, 0, 1, array[2][3]], #array[2][3]
                    [0, 0, 0, 1]])   
        outcome = mr.IKinSpace(Slist, M, T, thetalist, eomg, ev)
        joint1 = np.degrees(outcome[0][0])
        joint2 = np.degrees(outcome[0][1])
        joint3 = np.degrees(outcome[0][2])
        joint4 = np.degrees(outcome[0][3])
        if outcome[1] == True:
            if -90 <= joint1 <= 90 and -90 <= joint2 <= 90 and -90 <= joint3 <= 90:
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
                print("Moving to pick up block...")
                return np.array([joint1, joint2, joint3, ee_rotation-joint1, 1, 0.75, 0.75, 1.5])
                break
        else:
            print("No solution found")
            continue
    return np.array([0,0,0,0,0,0,0,0])

def desired_angle_config(Slist, M, thetalist):
    """
    Returns an array of desired joint configurations for the robot to move to
    """
    x,y,z,x_q,y_q,z_q,w_q = cam.closest_block()
    r = R.from_quat([x_q, y_q, z_q, w_q])
    rotation = r.as_euler('zyx', degrees=True)
    rotation_rad = (rotation[0] * np.pi / 180) % np.pi/2
    if rotation_rad > np.pi/4:
        rotation_rad = -rotation_rad % np.pi/4
    array = block_transformation(x,y,z)
    if array[0][3] >= 0.18:
        return newton_raphson(280,310,array, -rotation_rad)
    if array[0][3] >= 0.15:
        print("I am greater than 15")
        return newton_raphson(275,300,array, -rotation_rad)
    if array[0][3] < 0.13:
        print("I am less than 15")
        return newton_raphson(260,280, array, -rotation_rad)
    if array[0][3] < 0.15:
        return newton_raphson(265,295, array, -rotation_rad)
    
if __name__ == '__main__':
    #x,y,z = cam.get_xyz()
    #print(block_transformation(x,y,z))
    desired_angle_config(Slist, M, thetalist)
    #desired_angle_config(Slist,M,thetalist, block_transformation(x,y,z))
            