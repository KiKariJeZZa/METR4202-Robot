# METR4202-Robot

Welcome to Team 7s METR4202 Robot Repository.

## How to compile Team 7s code:

1. Git clone this repository to your local directory
2. First calibrate camera's location in the code using fiducials while runnning:
'''
roslaunch robot_hub setup.launch
'''
3. Now that camera's location is calibrated, run the following to execute robot:
'''
roslaunch robot_hub robot_hub.launch
'''
