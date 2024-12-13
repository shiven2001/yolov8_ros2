ROS2 workspace for NIRIS: Neurologically Intelligent Robot Inspection System

Full project name is PCU-NIRIS-NEPMDE: Project Chinese University Neurologically Intelligent Robot Inspection System for Navigation, Examination, and Predictive Maintenance of Dynamic Environments

Build and Tested on ROS2 Foxy.
Using Python 3.8.10

Add all the packages to your ROS2 workspace and then use:

```
cd ~/<niris_ws>/src
pip3 install -r requirements.txt
cd ~/<niris_ws>
rosdep install --from-paths src --ignore-src -r -y
colcon build
```

I am still developing the requirements.txt file.

##V1

The first version was build was yolobot. Yolobot robot was used to test and implement the integration of YOLOv8 with ROS2. It can be tested using:

```
cd ~/<niris_ws>
source install/setup.bash
ros2 launch yolobot_bringup yolobot.launch.py
```
