import subprocess


class ROSPackage:
    def __init__(self) -> None:
        self.package_name = str()
        self.node_name = str()
        self.class_name = str()
        self.namespace_name = str()

    def fill_template(self, filedata):
        filedata = filedata.replace('package_name_template', self.package_name)
        filedata = filedata.replace('node_name_template', self.node_name)
        filedata = filedata.replace('class_name_template', self.class_name)
        filedata = filedata.replace('namespace_template', self.namespace_name)
        return filedata

    def create_node(self):
        # Read in the file
        with open('templates/node_template.cpp', 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = self.fill_template(filedata)

        # Write the file out again
        with open('{}/src/{}/{}.cpp'.format(self.package_name, self.node_name, self.node_name), 'w') as file:
            file.write(filedata)

        # Read in the file
        with open('templates/main_template.cpp', 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = self.fill_template(filedata)

        # Write the file out again
        with open('{}/src/{}/{}_main.cpp'.format(self.package_name, self.node_name, self.node_name), 'w') as file:
            file.write(filedata)

        # Read in the file
        with open('templates/include_file_template.h', 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = self.fill_template(filedata)

        # Write the file out again
        with open('{}/include/{}.h'.format(self.package_name, self.node_name), 'w') as file:
            file.write(filedata)

    def edit_package(self):
        # Read in the file
        with open('templates/CMakeLists.txt', 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = self.fill_template(filedata)

        # Write the file out again
        with open('{}/CMakeLists.txt'.format(self.package_name), 'w') as file:
            file.write(filedata)

        # Read in the file
        with open('{}/package.xml'.format(self.package_name), 'r') as file:
            filedata = file.readlines()
        with open('templates/package_template.xml', 'r') as file:
            insertion_data = file.readlines()

        # Replace the target string
        filedata[53:53] = insertion_data

        # Write the file out again
        with open('{}/package.xml'.format(self.package_name), 'w') as file:
            file.writelines(filedata)

    def create_config(self):
        # Read in the file
        with open('templates/launch_template.launch', 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = self.fill_template(filedata)

        # Write the file out again
        with open('{}/launch/{}_launch.launch'.format(self.package_name, self.node_name), 'w') as file:
            file.write(filedata)

        subprocess.run(["cp templates/config_template.yaml {}/config/{}_config.yaml".format(
            self.package_name, self.node_name)], shell=True)
