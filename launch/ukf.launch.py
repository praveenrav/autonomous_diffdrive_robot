from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():

  # Set the path to UKF parameters: 
  ukf_params_file = '/home/praveenrav702/comp_ws/src/autonomous_diffdrive_robot/config/ukf.yaml'
                

  # Start robot localization using an Unscented Kalman filter
  ukf_node = Node(
    package='robot_localization',
    executable='ukf_node',
    name='ukf_filter_node',
    output='screen',
    parameters=[ukf_params_file, {'use_sim_time': True}],
    remappings=[
      ('/cmd_vel', '/diff_cont/cmd_vel_unstamped')
    ])

  return LaunchDescription([   
        ukf_node
    ])