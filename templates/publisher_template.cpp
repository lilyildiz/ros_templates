    //! publisher_name_template publisher.
    ros::Publisher m_publisher_name_template;
    

        m_publisher_name_template = m_node_handle.advertise<message_package_template::message_type_template>("topic_template", queue_template);
            