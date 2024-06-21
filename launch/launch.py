from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

PACKAGE_NAME = "ros2_laser_scan_matcher"
NODE_NAME = "laser_scan_matcher"

LASER_TRANSFORM_X = "0"
LASER_TRANSFORM_Y = "0.1"
LASER_TRANSFORM_Z = "0"

LASER_TRANSFORM_ROLL = "0"
LASER_TRANSFORM_PITCH = "0"
LASER_TRANSFORM_YAW = "0"


def generate_launch_description():
    ld = LaunchDescription()

    # Define a node to launch
    laser_scan_odom = Node(
        package=PACKAGE_NAME,
        executable=NODE_NAME,
        output="screen",
        # parameters=[config],
        parameters=[{"publish_odom": "laser_odom"}],
        # remappings=[("/original_topic", "/remapped_topic")],
    )

    # Define the static transform publisher
    static_transform_publisher = ExecuteProcess(
        cmd=[
            "ros2",
            "run",
            "tf2_ros",
            "static_transform_publisher",
            LASER_TRANSFORM_X,
            LASER_TRANSFORM_Y,
            LASER_TRANSFORM_Z,
            LASER_TRANSFORM_ROLL,
            LASER_TRANSFORM_PITCH,
            LASER_TRANSFORM_YAW,
            "base_link",
            "laser",
        ],
        output="screen",
    )

    ld.add_action(laser_scan_odom)
    ld.add_action(static_transform_publisher)

    return ld
