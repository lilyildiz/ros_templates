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
    class_name_template(ros::NodeHandle &t_node_handle);

  private:
    /*!
     * Reads and verifies the ROS parameters.
     * @return true if successful.
     */
    bool readParameters();

    //! ROS node handle.
    ros::NodeHandle &m_node_handle;

    //! Example parameter.
    std::string m_param;

    //--->Include insertion point <---
  };

} // namespace namespace_template