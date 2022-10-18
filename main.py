import blessed
import subprocess
import lib.ROSPackage
import lib.menu

options = lib.menu.run()
package = lib.ROSPackage.ROSPackage(options=options)

subprocess.run(["catkin_create_pkg {}".format(package.package_name)], shell=True)
subprocess.run(
    ["cd {} ;mkdir config include launch src ".format(package.package_name)], shell=True)
subprocess.run(
    ["cd {}/src ;mkdir {}".format(package.package_name, package.node_name)], shell=True)

package.create_node()
package.edit_package()
package.create_config()

