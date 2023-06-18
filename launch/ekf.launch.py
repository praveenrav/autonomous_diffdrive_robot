from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

  # Set the path to EKF parameters: 
  #ekf_params_file = os.path.join(get_package_share_directory('autonomous_diffdrive_robot'),'config','ekf.yaml')
  ekf_params_file = '/home/praveenrav702/comp_ws/src/autonomous_diffdrive_robot/config/ekf.yaml'
                

  # Start robot localization using an Extended Kalman filter
  ekf_node = Node(
    package='robot_localization',
    executable='ekf_node',
    name='ekf_filter_node',
    output='screen',
    parameters=[ekf_params_file, {'use_sim_time': True}],
    remappings=[
      ('/cmd_vel', '/diff_cont/cmd_vel_unstamped')
    ])

  return LaunchDescription([   
        ekf_node
    ])