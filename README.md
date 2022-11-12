
# ROS Template Generator

This project is used for creating basic ROS package templates in C++. 


## Dependencies

`console-menu`
## Package Example

A package created by this project will basically look like this

``` 
basic_package/
├── CMakeLists.txt
├── config
│   └── basic_node_config.yaml
├── include
│   └── basic_node.h
├── launch
│   └── basic_node_launch.launch
├── package.xml
└── src
    └── basic_node
        ├── basic_node.cpp
        └── basic_node_main.cpp
```

## Template

The basic template can be seen below. You can edit the template to your requirements and choose `XML Options` in the root menu to load your settings.

Another way to customize your package is the `Edit Package` section in the root menu. (not reccomended)

``` 
<?xml version="1.0"?>
    <package>
        <name>basic_package</name>
        <node>basic_node</node>
        <class>BasicNode</class>
        <namespace>BasicNamespace</namespace>
        <subscribers>
            <subscriber>
                <parent>BasicNode</parent>
                <name>BasicSub1</name>
                <topic>/foo</topic>
                <message_type_package>std_msgs</message_type_package>
                <message_type_type>Float64</message_type_type>
            </subscriber>
            <subscriber>
                <parent>BasicNode</parent>
                <name>BasicSub2</name>
                <topic>/foo</topic>
                <message_type_package>std_msgs</message_type_package>
                <message_type_type>Float64</message_type_type>
            </subscriber>
        </subscribers>
        <publishers>
            <publisher>
                <name>BasicPub</name>
                <topic>/foo2</topic>
                <message_type_package>std_msgs</message_type_package>
                <message_type_type>String</message_type_type>
            </publisher>
        </publishers>
    </package>
```

| Package Options | Description                 |
| :-------------- | :-------------------------- |
| name            | Package name                |
| node            | Node name                   |
| class           | Class name of the node      |
| namespace       | Namespace name of the class |

| Subscriber Options | Description                             |
| :----------------- | :-------------------------------------- |
| parent             | Parent class name for callback function |
| name               | Subscriber name                         |
| topic              | Topic name                              |
| msg_type_package   | Package name of the message type        |
| msg_type_type      | Message type name                       |

| Publisher Options | Description                      |
| :---------------- | :------------------------------- |
| name              | Publisher name                   |
| topic             | Topic name                       |
| msg_type_package  | Package name of the message type |
| msg_type_type     | Message type name                |

## Authors

- [@lilyildiz](https://github.com/lilyildiz)

