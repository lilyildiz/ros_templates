
# ROS Template Generator

This project is used for creating basic ROS package templates in C++. 


## Dependencies

`blessed`
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




## To Do

- Support for creating more than 1 node.

- <del>Support for creating more than 1 subscriber or publisher.</del>

- Support for creating action servers.

- Support for creating services.

- Support for generating custom ROS messages.



## Authors

- [@lilyildiz](https://github.com/lilyildiz)

