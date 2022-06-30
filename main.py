import blessed
import subprocess
import lib.helpers

term = blessed.Terminal()
package = lib.helpers.ROSPackage()

print(term.home + term.clear + term.move_y(term.height // 2))
print(term.black_on_darkkhaki(term.center('welcome to the ros template creater.')))
package.package_name = input(term.black_on_darkkhaki(term.center(
    'Please write the name of the package you want to create')))

subprocess.run(["catkin_create_pkg {}".format(package.package_name)], shell=True)
subprocess.run(
    ["cd {} ;mkdir config include launch src ".format(package.package_name)], shell=True)

print(term.home + term.clear + term.move_y(term.height // 2))
package.node_name = input(term.black_on_darkkhaki(term.center(
    'Please write the name of the node you want to create')))

print(term.home + term.clear + term.move_y(term.height // 2))
package.class_name = input(term.black_on_darkkhaki(term.center(
    'Please write the name of the class you want to create')))

print(term.home + term.clear + term.move_y(term.height // 2))
package.namespace_name = input(term.black_on_darkkhaki(term.center(
    'Please write the name of the namespace you want to create')))

subprocess.run(
    ["cd {}/src ;mkdir {}".format(package.package_name, package.node_name)], shell=True)


package.create_node()
package.edit_package()
package.create_config()

print(term.home + term.clear)
print(term.black_on_darkkhaki(term.center('package created successfully.')))
