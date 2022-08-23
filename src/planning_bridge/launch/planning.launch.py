import os
from launch import LaunchDescription
from launch_ros.actions import Node
 
def generate_launch_description():

    start_planning_client = Node(
        package='planning_bridge',
        executable='planning_client',
        output='screen')

    start_pose_server = Node(
        package='planning_bridge',
        executable='pose_server',
        output='screen')

    start_ugv_move = Node(
        package='planning_bridge',
        executable='ugv_move',
        output='screen')

    start_ugv_transporting_uav_move = Node(
        package='planning_bridge',
        executable='ugv_transporting_uav_move',
        output='screen')


    ld = LaunchDescription()
    ld.add_action(start_planning_client)
    ld.add_action(start_pose_server)
    ld.add_action(start_ugv_move)
    ld.add_action(start_ugv_transporting_uav_move)
 
    return ld