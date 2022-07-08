import subprocess
from . import ROSSubscriber
from . import ROSPublisher


class ROSPackage:
    def __init__(self) -> None:
        self.package_name = str()
        self.node_name = str()
        self.class_name = str()
        self.namespace_name = str()
        self.subscriber_amount = int()
        self.publisher_amount = int()

    def fill_template(self, filedata):
        filedata = filedata.replace('package_name_template', self.package_name)
        filedata = filedata.replace('node_name_template', self.node_name)
        filedata = filedata.replace('class_name_template', self.class_name)
        filedata = filedata.replace('namespace_template', self.namespace_name)
        return filedata

    def create_node(self):
        sub_include,sub_declaration,callback = self.createSubscribers(self.subscriber_amount)
        pub_include,pub_declaration = self.createPublishers(self.publisher_amount)

        # Create node file
        with open('templates/node_template.cpp', 'r') as file:
            filedata = file.read()

        filedata = self.fill_template(filedata)
        filedata = filedata.splitlines()

        declaration_index = [i for i, s in enumerate(filedata) if '--->Declaration insertion point <---' in s][0]
        filedata[declaration_index:declaration_index+1] = pub_declaration + sub_declaration
        callback_index = [i for i, s in enumerate(filedata) if '--->Callback insertion point <---' in s][0]
        filedata[callback_index:callback_index+1] = callback

        with open('{}/src/{}/{}.cpp'.format(self.package_name, self.node_name, self.node_name), 'w') as file:
            file.writelines(self.appendSeperator(filedata))

        # Create main file
        with open('templates/main_template.cpp', 'r') as file:
            filedata = file.read()

        filedata = self.fill_template(filedata)

        with open('{}/src/{}/{}_main.cpp'.format(self.package_name, self.node_name, self.node_name), 'w') as file:
            file.write(filedata)

        # Create include file
        with open('templates/include_file_template.h', 'r') as file:
            filedata = file.read()

        filedata = self.fill_template(filedata)
        filedata = filedata.splitlines()
        include_index = [i for i, s in enumerate(filedata) if '--->Include insertion point <---' in s][0]
        filedata[include_index:include_index+1] = pub_include + sub_include

        with open('{}/include/{}.h'.format(self.package_name, self.node_name), 'w') as file:
            file.writelines(self.appendSeperator(filedata))

    def edit_package(self):
        # Create CMakeLists
        with open('templates/CMakeLists.txt', 'r') as file:
            filedata = file.read()

        filedata = self.fill_template(filedata)

        with open('{}/CMakeLists.txt'.format(self.package_name), 'w') as file:
            file.write(filedata)

        # Create package.xml
        with open('templates/package_template.xml', 'r') as file:
            insertion_data = file.readlines()

        with open('{}/package.xml'.format(self.package_name), 'r+') as file:
            filedata = file.readlines()
            filedata[53:53] = insertion_data
            file.seek(0)
            file.writelines(filedata)
            

    def create_config(self):
        # Create launch
        with open('templates/launch_template.launch', 'r') as file:
            filedata = file.read()

        filedata = self.fill_template(filedata)

        with open('{}/launch/{}_launch.launch'.format(self.package_name, self.node_name), 'w') as file:
            file.write(filedata)

        # Copy .yaml file
        subprocess.run(["cp templates/config_template.yaml {}/config/{}_config.yaml".format(
            self.package_name, self.node_name)], shell=True)

    def createSubscribers(self,number):
        include,declaration,callback = list(),list(),list()
        for sub in range(number):
            temp = ROSSubscriber.ROSSubscriber(self.class_name,"subscriber{}".format(sub),"/subscribed_topic{}".format(sub))
            temp.createSubscriber()
            include += temp.include
            declaration += temp.declaration
            callback += temp.callback

        return include,declaration,callback

    def createPublishers(self,number):
        include,declaration = list(),list()
        for pub in range(number):
            temp = ROSPublisher.ROSPublisher("publisher{}".format(pub),"/published_topic{}".format(pub))
            temp.createPublisher()
            include += temp.include
            declaration += temp.declaration

        return include,declaration

    def appendSeperator(self,list):
        return [line+'\n' for line in list]
