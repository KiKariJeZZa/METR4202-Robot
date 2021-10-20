# METR4202-Robot

Welcome to Team 7s METR4202 Robot Repository.

## How to compile Team 7s code:

1. Git clone this repository to your local directory
2. Ensure USB limits are disabled prior to launching camera nodes with the following command
```
echo 0 | sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb
```
3. Run the following to start up the camera
```
roslaunch ximea_ros_cam example_cam.launch
```
4. Run the following to start up tag detection
```
roslaunch aruco_detect aruco_detect.launch camera:=/ximea_cam image:=/image_raw
```
5. Run the following in terminal to start up servos
```
roslaunch my_dynamixel_project dynamixel_interface_controller.launch
```
6. Finally run the main code in robot_hub to begin robot functionality
```
rosrun robot_hub main.py
```
