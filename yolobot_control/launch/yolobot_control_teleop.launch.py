import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        # Launch teleop_twist_keyboard in a new terminal
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'bash', '-c', 'ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/yolobot/cmd_vel; exec bash'],
            output='screen'
        ),
    ])