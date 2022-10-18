    /*!
     * subscriber_name_template callback method.
     * @param t_msg the received message.
     */
    void subscriber_name_templateCallback(const message_package_template::message_type_templateConstPtr &t_msg);

    //! subscriber_name_template subscriber.
    ros::Subscriber m_subscriber_name_template;

        m_subscriber_name_template = m_node_handle.subscribe("topic_template", freq_template, &class_name_template::subscriber_name_templateCallback, this);

    void class_name_template::subscriber_name_templateCallback(const message_package_template::message_type_templateConstPtr &t_msg)
    {
        ROS_INFO("subscriber_name_template recieved a message");
    }

#include <message_package_template/message_type_template.h>
