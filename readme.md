ROS2 workspace for NIRIS: Neurologically Intelligent Robot Inspection System

Full project name is PCU-NIRIS-NEPMDE:Project Chinese University Neurologically Intelligent Robot Inspection System for Navigation, Examination, and Predictive Maintenance of Dynamic Environments

Build and Tested on ROS2 Foxy

Add all the packages to your ROS2 workspace and then use:

`cd ~/<niris_ws>/src`
`pip3 install -r requirements.txt`
`cd ~/<niris_ws>`
`rosdep install --from-paths src --ignore-src -r -y`
`colcon build`

I am still developing the requirements.txt file.