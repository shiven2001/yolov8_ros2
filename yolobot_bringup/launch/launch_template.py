from launch import LaunchDescription
from launch_ros.actions import Node

# exactly this name!
def generate_launch_description():

    #instantiate a LaunchDescription object
    ld = LaunchDescription()

    topic_remap = ['', '']      # topic name, new topic name
    service_remap = ['', '']    # service name, new service name

    first_node = Node(

        package = '',     # package name

        executable = '',  # node's executable name

        name = '',        # if we want to remap the node name

        remappings = [topic_remap,
                      service_remap],     # if we want to remap topics or services names


        parameters = [{'parameter1': '',
                       'parameter2': ''}]  # declare parameters of the node <parameter_name> <default value> 
                                           # (if the value is not string, omit quotes
        )

    second_node = Node(
        ## same structure
    )

    # add as much nodes needed for your application

    # launch description
    ld.add_action(first_node)
    ld.add_action(second_node)

    return ld