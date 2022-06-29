#include <ros/ros.h>
#include "node_name_template.h"

namespace namespace_template
{
class_name_template::class_name_template(ros::NodeHandle& t_node_handle)
  : m_node_handle(t_node_handle)
{
    if (!readParameters())
    {
        ROS_ERROR("Could not read parameters.");
        ros::requestShutdown();
    }

    ROS_INFO("Input topic: : %s", m_input_topic.c_str());

    ROS_INFO("Output topic: : %s", m_output_topic.c_str());


    m_input_sub = m_node_handle.subscribe(m_input_topic, 10, &class_name_template::subCallback, this);

    m_output_pub =
        m_node_handle.advertise<std_msgs::String>(m_output_topic, 1000);

    ROS_INFO("Successfully launched node.");
}

bool class_name_template::readParameters()
{
    if (!m_node_handle.getParam("input_topic", m_input_topic))
    {
        return false;
    }
    if (!m_node_handle.getParam("output_topic", m_output_topic))
    {
        return false;
    }
    return true;
}

void class_name_template::subCallback(const std_msgs::String& t_msg)
{
    ROS_INFO("Recieved: : %s", t_msg.data.c_str());
    m_output_pub.publish(t_msg);
    ROS_INFO("Published the message.");
}
}  // namespace namespace_template