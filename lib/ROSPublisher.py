class ROSPublisher:
    def __init__(self) -> None:
        self.name = None
        self.topic = None
        self.queue = 1000
        self.message_type_package = None
        self.message_type_type = None
        self.include = None
        self.declaration = None


    def fill_template(self,filedata):
        filedata = filedata.replace('publisher_name_template', self.name)
        filedata = filedata.replace('topic_template', self.topic)
        filedata = filedata.replace('queue_template', str(self.queue))
        filedata = filedata.replace('message_package_template', self.message_type_package)
        filedata = filedata.replace('message_type_template',self.message_type_type)
        return filedata

    def createPublisher(self):
        # Create Publisher
        with open('templates/publisher_template.cpp', 'r') as file:
            filedata = file.read()

        filedata = self.fill_template(filedata)
        
        filedata = filedata.splitlines()

        self.include = filedata[:3]
        self.declaration = filedata[3:]

