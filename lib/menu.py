from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import PromptUtils
from consolemenu.format import *

import os
import xml.etree.ElementTree as ET

from . import ROSSubscriber
from . import ROSPublisher

class ROSAction:
    def __init__(self) -> None:
        self.name = None
        self.goal_message_package = None
        self.goal_message_type = None
        self.result_message_package = None
        self.result_message_type = None
        self.feedback_message_package = None
        self.feedback_message_type = None

class ROSService:
    def __init__(self) -> None:
        self.name = None
        self.request_message_package = None
        self.request_message_type = None
        self.response_message_package = None
        self.response_message_type = None

class ROSMessage:
    def __init__(self) -> None:
        self.name = None
        self.fields = []
        self.field_count = 0

class ROSPackageOptions:
    def __init__(self) -> None:
        self.package_name = None
        self.node_name = None
        self.class_name = None
        self.namespace_name = None
        self.subscriber_count = 0
        self.publisher_count = 0
        self.service_count = 0
        self.action_count = 0
        self.message_count = 0

        subscriber = ROSSubscriber.ROSSubscriber()
        publisher = ROSPublisher.ROSPublisher()
        service = ROSService()
        action = ROSAction()
        message = ROSMessage()
        self.subscribers = [subscriber]
        self.publishers = [publisher]
        self.services = [service]
        self.actions = [action]
        self.messages = [message]
    
    def ROSPackageOptions_to_XML(self,file_name):
        xml = """<?xml version="1.0"?>
    <package>
        <name>{package_name}</name>
        <node>{node_name}</node>
        <class>{class_name}</class>
        <namespace>{namespace_name}</namespace>
        <subscribers>""".format(package_name=self.package_name, node_name=self.node_name, class_name=self.class_name, namespace_name=self.namespace_name)
        for subscriber in self.subscribers[:-1]:
            xml += """
            <subscriber>
                <parent>{parent}</parent>
                <name>{name}</name>
                <topic>{topic}</topic>
                <message_type_package>{message_type_package}</message_type_package>
                <message_type_type>{message_type_type}</message_type_type>
            </subscriber>""".format(name=subscriber.name, topic=subscriber.topic, message_type_package=subscriber.message_type_package, message_type_type=subscriber.message_type_type)
        xml += """
        </subscribers>
        <publishers>"""
        for publisher in self.publishers[:-1]:
            xml += """
            <publisher>
                <name>{name}</name>
                <topic>{topic}</topic>
                <message_type_package>{message_type_package}</message_type_package>
                <message_type_type>{message_type_type}</message_type_type>
            </publisher>""".format(name=publisher.name, topic=publisher.topic, message_type_package=publisher.message_type_package, message_type_type=publisher.message_type_type)
        xml += """
        </publishers>
    </package>"""

        with open(file_name, 'w') as f:
            f.write(xml)


    def ROSPackageOptions_from_XML(self, xml):
        self.package_name = xml.find('name').text
        self.node_name = xml.find('node').text
        self.class_name = xml.find('class').text
        self.namespace_name = xml.find('namespace').text
        self.subscriber_count = len(xml.find('subscribers').findall('subscriber'))
        self.publisher_count = len(xml.find('publishers').findall('publisher'))
        # self.service_count = len(xml.find('services').findall('service'))
        # self.action_count = len(xml.find('actions').findall('action'))
        # self.message_count = len(xml.find('messages').findall('message'))
        subscriber = ROSSubscriber.ROSSubscriber()
        publisher = ROSPublisher.ROSPublisher()
        service = ROSService()
        action = ROSAction()
        message = ROSMessage()
        self.subscribers = [subscriber]
        self.publishers = [publisher]
        self.services = [service]
        self.actions = [action]
        self.messages = [message]
        for xml_subscriber in xml.find('subscribers').findall('subscriber'):
            subscriber = ROSSubscriber.ROSSubscriber()
            subscriber.parent = xml_subscriber.find('parent').text
            subscriber.name = xml_subscriber.find('name').text
            subscriber.topic = xml_subscriber.find('topic').text
            subscriber.message_type_package = xml_subscriber.find('message_type_package').text
            subscriber.message_type_type = xml_subscriber.find('message_type_type').text
            self.subscribers.insert(0,subscriber)
        for xml_publisher in xml.find('publishers').findall('publisher'):
            publisher = ROSPublisher.ROSPublisher()
            publisher.name = xml_publisher.find('name').text
            publisher.topic = xml_publisher.find('topic').text
            publisher.message_type_package = xml_publisher.find('message_type_package').text
            publisher.message_type_type = xml_publisher.find('message_type_type').text
            self.publishers.insert(0,publisher)
        # for xml_service in xml.find('services').findall('service'):
        #     service = ROSService()
        #     service.name = xml_service.find('name').text
        #     self.services.insert(0,service)
        # for xml_action in xml.find('actions').findall('action'):
        #     action = ROSAction()
        #     action.name = xml_action.find('name').text
        #     self.actions.insert(0,action)
        # for xml_message in xml.find('messages').findall('message'):
        #     message = ROSMessage()
        #     message.name = xml_message.find('name').text
        #     self.messages.insert(0,message)  






        


getattr_string = lambda object,key: getattr(object,key) if getattr(object,key) is not None else "None"

def get_input_string(object,key):
    while True:
        print("Current value: " + getattr_string(object,key))
        setattr(object,key,input("Enter a value: "))
        if key == "":
            print("Please enter a value")
        else:
            return 

def get_subscriber_input_string(key):
    while True:
        print("Current value: " + getattr_string(ros_package_options.subscribers[-1],key))
        setattr(ros_package_options.subscribers[-1],key,input("Enter a value: "))
        if key == "":
            print("Please enter a value")
        else:
            return 

def get_publisher_input_string(key):
    while True:
        print("Current value: " + getattr_string(ros_package_options.publishers[-1],key))
        setattr(ros_package_options.publishers[-1],key,input("Enter a value: "))
        if key == "":
            print("Please enter a value")
        else:
            return

def get_service_input_string(key):
    while True:
        print("Current value: " + getattr_string(ros_package_options.services[-1],key))
        setattr(ros_package_options.services[-1],key,input("Enter a value: "))
        if key == "":
            print("Please enter a value")
        else:
            return

def get_action_input_string(key):
    while True:
        print("Current value: " + getattr_string(ros_package_options.actions[-1],key))
        setattr(ros_package_options.actions[-1],key,input("Enter a value: "))
        if key == "":
            print("Please enter a value")
        else:
            return

def get_message_input_string(key):
    while True:
        print("Current value: " + getattr_string(ros_package_options.messages[-1],key))
        setattr(ros_package_options.messages[-1],key,input("Enter a value: "))
        if key == "":
            print("Please enter a value")
        else:
            return

def root_menu_subtitle():
    return  """
    Package Name: {ros_package_options.package_name}
    Node Name: {ros_package_options.node_name}
    Class Name: {ros_package_options.class_name}
    Namespace Name: {ros_package_options.namespace_name}
    Subscriber Count: {ros_package_options.subscriber_count}
    Publisher Count: {ros_package_options.publisher_count}
    """.format(ros_package_options=ros_package_options)

def subscriber_submenu_subtitle() -> str:
    return """
    Parent Name: {subscriber.parent}
    Name: {subscriber.name}
    Topic: {subscriber.topic}
    Message Package: {subscriber.message_type_package}
    Message Type: {subscriber.message_type_type}
    """.format(subscriber=ros_package_options.subscribers[-1])

def publisher_submenu_subtitle() -> str:
    return """
    Name: {publisher.name}
    Topic: {publisher.topic}
    Message Package: {publisher.message_type_package}
    Message Type: {publisher.message_type_type}
    """.format(publisher=ros_package_options.publishers[-1])

def service_submenu_subtitle() -> str:
    return """
    Name: {service.name}
    """.format(service=ros_package_options.services[-1])

def action_submenu_subtitle() -> str:
    return """
    Name: {action.name}
    """.format(action=ros_package_options.actions[-1])

def message_submenu_subtitle() -> str:
    return """
    Name: {message.name}
    """.format(message=ros_package_options.messages[-1])

def remove_subscriber_submenu_subtitle() -> str:
    return """ Please write the name of the subscriber you want to remove:
    Current Subscribers:    {subscribers}

    """.format(subscribers=', '.join([subscriber.name for subscriber in ros_package_options.subscribers][:-1]))

def remove_publisher_submenu_subtitle() -> str:
    return """ Please write the name of the publisher you want to remove:
    Current Publishers:    {publishers}

    """.format(publishers=', '.join([publisher.name for publisher in ros_package_options.publishers][:-1]))

def remove_service_submenu_subtitle() -> str:
    return """ Please write the name of the service you want to remove:
    Current Services:    {services}

    """.format(services=', '.join([service.name for service in ros_package_options.services][:-1]))

def remove_action_submenu_subtitle() -> str:
    return """ Please write the name of the action you want to remove:
    Current Actions:    {actions}

    """.format(actions=', '.join([action.name for action in ros_package_options.actions][:-1]))

def remove_message_submenu_subtitle() -> str:
    return """ Please write the name of the message you want to remove:
    Current Messages:    {messages}

    """.format(messages=', '.join([message.name for message in ros_package_options.messages][:-1]))

def add_subscriber(menu):
    if check_subscriber_filled():
        subscriber = ROSSubscriber.ROSSubscriber()
        ros_package_options.subscribers.append(subscriber)
        ros_package_options.subscriber_count += 1
        print(added_subscriber_succesfully_message())
        PromptUtils(Screen()).enter_to_continue()
    menu.clear_screen()

def added_subscriber_succesfully_message() -> str:
    return """
    Subscriber added succesfully
    Subscriber Parent: {subscriber.parent}
    Subsriber Name: {subscriber.name}
    Subscriber Topic: {subscriber.topic}
    Subscriber Message Package: {subscriber.message_type_package}
    Subscriber Message Type: {subscriber.message_type_type}
    """.format(subscriber=ros_package_options.subscribers[-2])

def check_subscriber_filled():
    if ros_package_options.subscribers[-1].parent is None:
        print("Please enter a parent name")
        PromptUtils(Screen()).enter_to_continue()
        return False
    if ros_package_options.subscribers[-1].name is None:
        print("Please enter a name")
        PromptUtils(Screen()).enter_to_continue()
        return False
    if ros_package_options.subscribers[-1].topic is None:
        print("Please enter a topic")
        PromptUtils(Screen()).enter_to_continue()
        return False
    if ros_package_options.subscribers[-1].message_type_package is None:
        print("Please enter a message type package")
        PromptUtils(Screen()).enter_to_continue()
        return False
    if ros_package_options.subscribers[-1].message_type_type is None:
        print("Please enter a message type")
        PromptUtils(Screen()).enter_to_continue()
        return False
    return True

def remove_subscriber(menu):
    name = input(remove_subscriber_submenu_subtitle())
    for subscriber in ros_package_options.subscribers:
        if subscriber.name == name:
            ros_package_options.subscribers.remove(subscriber)
            ros_package_options.subscriber_count -= 1
            break
    else:
        print("Subscriber not found")
    menu.clear_screen()
    
def add_publisher(menu):
    if check_publisher_filled():
        publisher = ROSPublisher.ROSPublisher()
        ros_package_options.publishers.append(publisher)
        ros_package_options.publisher_count += 1
        print(added_publisher_successfully_message())
        PromptUtils(Screen()).enter_to_continue()
    menu.clear_screen()

def added_publisher_successfully_message() -> str:
    return """
    Publisher added successfully
    Publisher Name: {publisher.name}
    Publisher Topic: {publisher.topic}
    Publisher Message Package: {publisher.message_type_package}
    Publisher Message Type: {publisher.message_type_type}
    """.format(publisher=ros_package_options.publishers[-2])

def check_publisher_filled():
    if ros_package_options.publishers[-1].name is None:
        print("Please enter a name")
        PromptUtils(Screen()).enter_to_continue()
        return False
    if ros_package_options.publishers[-1].topic is None:
        print("Please enter a topic")
        PromptUtils(Screen()).enter_to_continue()
        return False
    if ros_package_options.publishers[-1].message_type_package is None:
        print("Please enter a message type package")
        PromptUtils(Screen()).enter_to_continue()
        return False
    if ros_package_options.publishers[-1].message_type_type is None:
        print("Please enter a message type")
        PromptUtils(Screen()).enter_to_continue()
        return False
    return True

def remove_publisher(menu):
    name = input(remove_publisher_submenu_subtitle())
    for publisher in ros_package_options.publishers:
        if publisher.name == name:
            ros_package_options.publishers.remove(publisher)
            ros_package_options.publisher_count -= 1
            break
    else:
        print("Publisher not found")
    menu.clear_screen()

def add_service(menu):
    if check_service_filled():
        service = ROSService()
        ros_package_options.services.append(service)
        ros_package_options.service_count += 1
        print(added_service_successfully_message())
        PromptUtils(Screen()).enter_to_continue()
    menu.clear_screen()

def added_service_successfully_message() -> str:
    return """
    Service added successfully
    Service Name: {service.name}
    """.format(service=ros_package_options.services[-2])

def check_service_filled():
    if ros_package_options.services[-1].name is None:
        print("Please enter a name")
        PromptUtils(Screen()).enter_to_continue()
        return False
    return True

def remove_service(menu):
    name = input(remove_service_submenu_subtitle())
    for service in ros_package_options.services:
        if service.name == name:
            ros_package_options.services.remove(service)
            ros_package_options.service_count -= 1
            break
    else:
        print("Service not found")
    menu.clear_screen()

def add_action(menu):
    if check_action_filled():
        action = ROSAction()
        ros_package_options.actions.append(action)
        ros_package_options.action_count += 1
        print(added_action_successfully_message())
        PromptUtils(Screen()).enter_to_continue()
    menu.clear_screen()

def added_action_successfully_message() -> str:   
    return """
    Action added successfully
    Action Name: {action.name}
    """.format(action=ros_package_options.actions[-2])

def check_action_filled():
    if ros_package_options.actions[-1].name is None:
        print("Please enter a name")
        PromptUtils(Screen()).enter_to_continue()
        return False
    return True

def remove_action(menu):
    name = input(remove_action_submenu_subtitle())
    for action in ros_package_options.actions:
        if action.name == name:
            ros_package_options.actions.remove(action)
            ros_package_options.action_count -= 1
            break
    else:
        print("Action not found")
    menu.clear_screen()

def add_message(menu):
    if check_message_filled():
        message = ROSMessage()
        ros_package_options.messages.append(message)
        ros_package_options.message_count += 1
        print(added_message_successfully_message())
        PromptUtils(Screen()).enter_to_continue()
    menu.clear_screen()

def added_message_successfully_message() -> str:
    return """
    Message added successfully
    Message Name: {message.name}
    """.format(message=ros_package_options.messages[-2])

def check_message_filled():
    if ros_package_options.messages[-1].name is None:
        print("Please enter a name")
        PromptUtils(Screen()).enter_to_continue()
        return False
    return True

def remove_message(menu):
    name = input(remove_message_submenu_subtitle())
    for message in ros_package_options.messages:
        if message.name == name:
            ros_package_options.messages.remove(message)
            ros_package_options.message_count -= 1
            break
    else:
        print("Message not found")
    menu.clear_screen()

def get_remove_subscriber_options():
    menu = ConsoleMenu(title="Remove Subscriber Options", subtitle=remove_subscriber_submenu_subtitle,exit_option_text='Go Back')
    menu.append_item(FunctionItem("Remove", remove_subscriber, args=[menu]))
    menu.show(show_exit_option=True)
    return 

def get_remove_publiser_options():
    menu = ConsoleMenu(title="Remove Publisher Options", subtitle=remove_publisher_submenu_subtitle,exit_option_text='Go Back')
    menu.append_item(FunctionItem("Remove", remove_publisher, args=[menu]))
    menu.show(show_exit_option=True)
    return

def get_remove_service_options():
    menu = ConsoleMenu(title="Remove Service Options", subtitle=remove_service_submenu_subtitle,exit_option_text='Go Back')
    menu.append_item(FunctionItem("Remove", remove_service, args=[menu]))
    menu.show(show_exit_option=True)
    return

def get_remove_action_options():
    menu = ConsoleMenu(title="Remove Action Options", subtitle=remove_action_submenu_subtitle,exit_option_text='Go Back')
    menu.append_item(FunctionItem("Remove", remove_action, args=[menu]))
    menu.show(show_exit_option=True)
    return

def get_remove_message_options():
    menu = ConsoleMenu(title="Remove Message Options", subtitle=remove_message_submenu_subtitle,exit_option_text='Go Back')
    menu.append_item(FunctionItem("Remove", remove_message, args=[menu]))
    menu.show(show_exit_option=True)
    return

def get_subscriber_options() -> ROSSubscriber:
    menu = ConsoleMenu(title="Subscriber Options", subtitle=subscriber_submenu_subtitle,exit_option_text='Go Back')
    menu.append_item(FunctionItem("Parent Name", get_subscriber_input_string, args=['parent']))
    menu.append_item(FunctionItem("Name", get_subscriber_input_string, args=['name']))
    menu.append_item(FunctionItem("Topic", get_subscriber_input_string, args=['topic']))
    menu.append_item(FunctionItem("Message Package", get_subscriber_input_string, args=['message_type_package']))
    menu.append_item(FunctionItem("Message Type", get_subscriber_input_string, args=['message_type_type']))
    menu.append_item(FunctionItem("Add Subscriber", add_subscriber, args=[menu]))
    menu.show(show_exit_option=True)
    return  

def get_publisher_options() -> ROSPublisher:
    menu = ConsoleMenu(title="Publisher Options", subtitle=publisher_submenu_subtitle,exit_option_text='Go Back')
    menu.append_item(FunctionItem("Name", get_publisher_input_string, args=['name']))
    menu.append_item(FunctionItem("Topic", get_publisher_input_string, args=['topic']))
    menu.append_item(FunctionItem("Message Package", get_publisher_input_string, args=['message_type_package']))
    menu.append_item(FunctionItem("Message Type", get_publisher_input_string, args=['message_type_type']))
    menu.append_item(FunctionItem("Add Publisher", add_publisher, args=[menu]))
    menu.show(show_exit_option=True)
    return

def get_service_options() -> ROSService:
    menu = ConsoleMenu(title="Service Options", subtitle=service_submenu_subtitle,exit_option_text='Go Back')
    menu.append_item(FunctionItem("Name", get_service_input_string, args=['name']))
    menu.append_item(FunctionItem("Add Service", add_service, args=[menu]))
    menu.show(show_exit_option=True)
    return

def get_action_options() -> ROSAction:
    menu = ConsoleMenu(title="Action Options", subtitle=action_submenu_subtitle,exit_option_text='Go Back')
    menu.append_item(FunctionItem("Name", get_action_input_string, args=['name']))
    menu.append_item(FunctionItem("Add Action", add_action, args=[menu]))
    menu.show(show_exit_option=True)
    return

def get_message_options() -> ROSMessage:
    menu = ConsoleMenu(title="Message Options", subtitle=message_submenu_subtitle,exit_option_text='Go Back')
    menu.append_item(FunctionItem("Name", get_message_input_string, args=['name']))
    menu.append_item(FunctionItem("Add Message", add_message, args=[menu]))
    menu.show(show_exit_option=True)
    return

def add_remove_sub_pub_options():
    menu = ConsoleMenu(title="Add/Remove Subscribers/Publishers", subtitle=root_menu_subtitle)
    menu.append_item(FunctionItem("Add Subscriber", get_subscriber_options))
    menu.append_item(FunctionItem("Remove Subscriber", get_remove_subscriber_options))
    menu.append_item(FunctionItem("Add Publisher", get_publisher_options))
    menu.append_item(FunctionItem("Remove Publisher", get_remove_publiser_options))
    return menu

def add_remove_service_action_message_options():
    menu = ConsoleMenu(title="Add/Remove Services/Actions/Messages", subtitle=root_menu_subtitle)
    menu.append_item(FunctionItem("Add Service", get_service_options))
    menu.append_item(FunctionItem("Remove Service", get_remove_service_options))
    menu.append_item(FunctionItem("Add Action", get_action_options))
    menu.append_item(FunctionItem("Remove Action", get_remove_action_options))
    menu.append_item(FunctionItem("Add Message", get_message_options))
    menu.append_item(FunctionItem("Remove Message", get_remove_message_options))
    return menu

def get_xml_file_input():
    file_name = input("Please enter the name of the file to load from: ")
    if not os.path.isfile(file_name):
        print("File not found")
        PromptUtils(Screen()).enter_to_continue()
        return None
    else:
        tree = ET.parse(file_name)
        root = tree.getroot()
        ros_package_options.ROSPackageOptions_from_XML(root)

def generate_xml_file():
    file_name = input("Please enter the name of the file to save to: ")
    if os.path.isfile(file_name):
        print("File already exists")
        PromptUtils(Screen()).enter_to_continue()
        return None
    else:
        ros_package_options.ROSPackageOptions_to_XML(file_name)
        print("File saved successfully")
        PromptUtils(Screen()).enter_to_continue()
        return None


def get_xml_options():
    menu = ConsoleMenu(title="XML Options", subtitle="Write or Read from XML file",exit_option_text='Go Back')
    menu.append_item(FunctionItem("Load From XML File", get_xml_file_input))
    menu.append_item(FunctionItem("Generate XML", generate_xml_file))
    return menu

def get_input_options():
    object = ros_package_options
    menu = ConsoleMenu(title="Edit Package", subtitle=root_menu_subtitle,exit_option_text='Go Back')
    menu.append_item(FunctionItem("Package Name", get_input_string, args=[object,'package_name']))
    menu.append_item(FunctionItem("Node Name", get_input_string, args=[object,'node_name']))
    menu.append_item(FunctionItem("Class Name", get_input_string, args=[object,'class_name']))
    menu.append_item(FunctionItem("Namespace Name", get_input_string, args=[object,'namespace_name']))

    submenu_1 = add_remove_sub_pub_options()
    submenu_1 = SubmenuItem("Add/Remove Subscribers/Publishers", submenu_1)
    submenu_1.set_menu(menu)

    menu.append_item(submenu_1)
    return menu

def get_ros_package_options(object) -> ROSPackageOptions:
    menu = ConsoleMenu(title="ROS Template Generator", subtitle=root_menu_subtitle,exit_option_text='Create Package')

    submenu_1 = get_input_options()
    submenu_1 = SubmenuItem("Edit Package", submenu_1)
    submenu_1.set_menu(menu)

    # Disabled for now
    # submenu_2 = add_remove_service_action_message_options()
    # submenu_2 = SubmenuItem("Add/Remove Services/Actions/Messages", submenu_2)
    # submenu_2.set_menu(menu)

    submenu_3 = get_xml_options()
    submenu_3 = SubmenuItem("XML Options", submenu_3)
    submenu_3.set_menu(menu)

    menu.append_item(submenu_1)
    # menu.append_item(submenu_2)
    menu.append_item(submenu_3)

    menu.start()
    menu.join()
    return

def check_package_filled(object):
    if object.package_name is None or object.package_name == '':
        print("Package name not filled")
        PromptUtils(Screen()).enter_to_continue()
        return False
    if object.node_name is None or object.node_name == '':
        print("Node name not filled")
        PromptUtils(Screen()).enter_to_continue()
        return False
    if object.class_name is None or object.class_name == '':
        print("Class name not filled")
        PromptUtils(Screen()).enter_to_continue()
        return False
    if object.namespace_name is None or object.namespace_name == '':
        print("Namespace name not filled")
        PromptUtils(Screen()).enter_to_continue()
        return False
    return True

def run():
    get_ros_package_options(ros_package_options)
    while not check_package_filled(ros_package_options):
        get_ros_package_options(ros_package_options)
    return ros_package_options

ros_package_options = ROSPackageOptions()
