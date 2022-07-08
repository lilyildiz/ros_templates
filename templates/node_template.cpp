#include <ros/ros.h>
#include "node_name_template.h"

namespace namespace_template
{
    class_name_template::class_name_template(ros::NodeHandle &t_node_handle)
        : m_node_handle(t_node_handle)
    {
        if (!readParameters())
        {
            ROS_ERROR("Could not read parameters.");
            ros::requestShutdown();
        }

        ROS_INFO("Example param: %s", m_param.c_str());

        //--->Declaration insertion point <---


        ROS_INFO("Successfully launched node.");
    }

    bool class_name_template::readParameters()
    {
        if (!m_node_handle.getParam("example", m_param))
        {
            return false;
        }
        return true;
    }

    //--->Callback insertion point <---
} // namespace namespace_template