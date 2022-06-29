#include <ros/ros.h>
#include "node_name_template.h"

int main(int argc , char **argv) 
{
    ros::init(argc, argv, "node_name_template");
    ros::NodeHandle node_handle("~");

    namespace_template::class_name_template class_name_template(node_handle);

    ros::spin();
    return 0;
}
