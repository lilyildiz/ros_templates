import subprocess

def fill_template(filedata,name_list):
    filedata = filedata.replace('package_name_template', name_list[0])
    filedata = filedata.replace('node_name_template', name_list[1])
    filedata = filedata.replace('class_name_template', name_list[2])
    filedata = filedata.replace('namespace_template', name_list[3])
    return filedata

def create_node(name_list):
    # Read in the file
    with open('templates/node_template.cpp', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = fill_template(filedata,name_list)

    # Write the file out again
    with open('{}/src/{}/{}.cpp'.format(name_list[0],name_list[1],name_list[1]), 'w') as file:
        file.write(filedata)


    # Read in the file
    with open('templates/main_template.cpp', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = fill_template(filedata,name_list)

    # Write the file out again
    with open('{}/src/{}/{}_main.cpp'.format(name_list[0],name_list[1],name_list[1]), 'w') as file:
        file.write(filedata)

    # Read in the file
    with open('templates/include_file_template.h', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = fill_template(filedata,name_list)

    # Write the file out again
    with open('{}/include/{}.h'.format(name_list[0],name_list[1]), 'w') as file:
        file.write(filedata)

def edit_package(name_list):
    # Read in the file
    with open('templates/CMakeLists.txt', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = fill_template(filedata,name_list)

    # Write the file out again
    with open('{}/CMakeLists.txt'.format(name_list[0]), 'w') as file:
        file.write(filedata)


    # Read in the file
    with open('{}/package.xml'.format(name_list[0]), 'r') as file :
        filedata = file.readlines()
    with open('templates/package_template.xml', 'r') as file :
        insertion_data = file.readlines()

    # Replace the target string
    filedata[53:53] = insertion_data

    # Write the file out again
    with open('{}/package.xml'.format(name_list[0]), 'w') as file:
        file.writelines(filedata)

def create_config(name_list):
    # Read in the file
    with open('templates/launch_template.launch', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = fill_template(filedata,name_list)

    # Write the file out again
    with open('{}/launch/{}_launch.launch'.format(name_list[0],name_list[1]), 'w') as file:
        file.write(filedata)

    subprocess.run(["cp templates/config_template.yaml {}/config/{}_config.yaml".format(name_list[0],name_list[1])], shell=True)