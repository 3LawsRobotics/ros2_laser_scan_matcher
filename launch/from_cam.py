from launch import LaunchDescription
from launch_ros.actions import Node

PACKAGE_NAME = "ros2_laser_scan_matcher"
NODE_NAME = "laser_scan_matcher_from_cam"


def generate_launch_description():
    ld = LaunchDescription()

    # Define a node to launch
    laser_scan_odom = Node(
        package=PACKAGE_NAME,
        executable=NODE_NAME,
        output="screen",
        # parameters=[config],
        parameters=[{"publish_odom": "camera_odom", "laser_frame": "/camera_link"}],
        remappings=[("/scan", "/camera_scan")],
    )

    ld.add_action(laser_scan_odom)

    return ld
