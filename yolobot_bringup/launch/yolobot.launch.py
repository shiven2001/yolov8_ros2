#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess


def generate_launch_description():

    pkg_yolobot_gazebo = get_package_share_directory('yolobot_gazebo')
    pkg_yolobot_description = get_package_share_directory('yolobot_description')
    pkg_yolobot_control = get_package_share_directory('yolobot_control')
    pkg_yolobot_recognition = get_package_share_directory('yolobot_recognition')

    # Joystick node if controlling using joystick
    joy_node = Node(
        package = "joy",
        executable = "joy_node"
    )

    start_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_yolobot_gazebo, 'launch', 'start_world.launch.py'),
        )
    )

    spawn_robot_in_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_yolobot_description, 'launch', 'spawn_yolobot.launch.py'),
        )
    )


    spawn_robot_control_joy = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_yolobot_control, 'launch', 'yolobot_control_joy.launch.py'),
        )
    )  

    spawn_robot_control_teleop = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_yolobot_control, 'launch', 'yolobot_control_teleop.launch.py'),
        )
    )  

    spawn_yolo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_yolobot_recognition, 'launch', 'yolov8.launch.py'),
        )
    )  

    return LaunchDescription([
        start_world,
        spawn_robot_in_world,
        spawn_robot_control_teleop,
        spawn_yolo
    ])