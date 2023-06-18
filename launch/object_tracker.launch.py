import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch.actions import DeclareLaunchArgument

def generate_launch_description():

    package_name='autonomous_diffdrive_robot'
    sim_mode = LaunchConfiguration('sim_mode')
    sim_mode_dec = DeclareLaunchArgument('sim_mode', default_value='false')

    tuning_mode = LaunchConfiguration('tuning_mode')
    tuning_mode_dec = DeclareLaunchArgument('tuning_mode', default_value='true')

    tracker_params_sim = os.path.join(get_package_share_directory(package_name), 'config', 'object_tracker_params_sim.yaml')
    #tracker_params_robot = os.path.join(get_package_share_directory(package_name), 'config', 'object_tracker_params_robot.yaml')
    tracker_params_robot = '/home/praveenrav702/comp_ws/src/autonomous_diffdrive_robot/config/object_tracker_params_robot.yaml'
    
    params_path = PythonExpression(['"',tracker_params_sim, '" if "true" == "', sim_mode, '" else "', tracker_params_robot, '"'])
    
    tracker_launch = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('object_tracker'), 'launch', 'object_tracker.launch.py')]),
                    launch_arguments={'params_file': params_path,
                                      'tune_detection': tuning_mode,
                                    'image_topic': '/image_raw'}.items())




    return LaunchDescription([
        sim_mode_dec,
        tuning_mode_dec,
        tracker_launch,
    ])