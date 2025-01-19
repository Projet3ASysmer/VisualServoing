#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    video_node = Node(
	namespace="bluerov2",
        package="autonomous_rov",
        executable="video",
    )
    
        # Define nodes
    image_processing_tracker_node = Node(
	namespace="bluerov2",   
        package='autonomous_rov',
        executable='image_processing_tracker',
        output='screen',
    )
    
    # Create the launch description and populate
    ld = LaunchDescription()
    
    ld.add_action(video_node)
    ld.add_action(image_processing_tracker_node)

    return ld
