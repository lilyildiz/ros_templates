class ROSSubscriber:
    def __init__(self) -> None:
        self.parent = None
        self.name = None
        self.topic = None
        self.freq = 10
        self.message_type_package = None
        self.message_type_type = None
        self.include = None
        self.declaration = None
        self.callback = None

    def fill_template(self,filedata):
        filedata = filedata.replace('class_name_template', self.parent)
        filedata = filedata.replace('subscriber_name_template', self.name)
        filedata = filedata.replace('topic_template', self.topic)
        filedata = filedata.replace('freq_template', str(self.freq))
        filedata = filedata.replace('message_package_template', self.message_type_package)
        filedata = filedata.replace('message_type_template',self.message_type_type)
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
