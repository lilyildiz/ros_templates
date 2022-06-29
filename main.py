import blessed
import subprocess
import lib.helpers

term = blessed.Terminal()

print(term.home + term.clear + term.move_y(term.height // 2))
print(term.black_on_darkkhaki(term.center('welcome to the ros template creater.')))
package_name = input(term.black_on_darkkhaki(term.center('Please write the name of the package you want to create')))

subprocess.run(["catkin_create_pkg {}".format(package_name)], shell=True)
subprocess.run(["cd {} ;mkdir config include launch src ".format(package_name)], shell=True)

print(term.home + term.clear + term.move_y(term.height // 2))
node_name = input(term.black_on_darkkhaki(term.center('Please write the name of the node you want to create')))

print(term.home + term.clear + term.move_y(term.height // 2))
class_name = input(term.black_on_darkkhaki(term.center('Please write the name of the class you want to create')))

print(term.home + term.clear + term.move_y(term.height // 2))
namespace_name = input(term.black_on_darkkhaki(term.center('Please write the name of the namespace you want to create')))

subprocess.run(["cd {}/src ;mkdir {}".format(package_name,node_name)], shell=True)

name_list = [package_name,node_name,class_name,namespace_name]

lib.helpers.create_node(name_list)
lib.helpers.edit_package(name_list)
lib.helpers.create_config(name_list)

print(term.home + term.clear)
print(term.black_on_darkkhaki(term.center('package created successfully.')))