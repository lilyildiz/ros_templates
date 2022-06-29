#pragma once

#include <ros/ros.h>
#include "std_msgs/String.h"

namespace namespace_template
{
class class_name_template
{
  public:
    /*!
     * Constructor.
     * @param nodeHandle the ROS node handle.
     */
    class_name_template(ros::NodeHandle& t_node_handle);

  private:
    /*!
     * Reads and verifies the ROS parameters.
     * @return true if successful.
     */
    bool readParameters();

    /*!
     * Odometry callback method.
     * @param t_Odom the received message.
     */
    void subCallback(const std_msgs::String& t_msg);

    //! ROS node handle.
    ros::NodeHandle& m_node_handle;

    //! Input topic name.
    std::string m_input_topic;

    //! Output topic name.
    std::string m_output_topic;

    //! Input subscriber.
    ros::Subscriber m_input_sub;

    //! Output publisher.
    ros::Publisher m_output_pub;

};

}  // namespace namespace_template