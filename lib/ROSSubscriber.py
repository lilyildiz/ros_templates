class MessageType:
    def __init__(self) -> None:
        self.package = 'std_msgs'
        self.type = 'String'

class ROSSubscriber:
    def __init__(self,parent_name,name,topic) -> None:
        self.parent = parent_name
        self.name = name
        self.topic = topic
        self.freq = 10
        self.message_type = MessageType()
        self.include = None
        self.declaration = None
        self.callback = None

    def fill_template(self,filedata):
        filedata = filedata.replace('class_name_template', self.parent)
        filedata = filedata.replace('subscriber_name_template', self.name)
        filedata = filedata.replace('topic_template', self.topic)
        filedata = filedata.replace('freq_template', str(self.freq))
        filedata = filedata.replace('message_package_template', self.message_type.package)
        filedata = filedata.replace('message_type_template',self.message_type.type)
        return filedata

    def createSubscriber(self):
        # Create Subscriber
        with open('templates/subscriber_template.cpp', 'r') as file:
            filedata = file.read()

        filedata = self.fill_template(filedata)
        
        filedata = filedata.splitlines()

        self.include = filedata[:9]
        self.declaration = filedata[8:11]
        self.callback = filedata[11:]
