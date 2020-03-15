import yaml
import sys
import global_finder
from subprocess import Popen, PIPE

found_globals, tree = global_finder.find_globals(sys.stdin)

data = yaml.safe_load(open("lookups.yml").read())
for found in found_globals:
    if found in ["print", "__name__"]:
        continue
    if found in data:
        package = data[found]["package"]
        print("from {} import {}".format(package, found))
        if "pip" in data[found]:
            pip = Popen(["/usr/bin/pip3", "install",  "{}".format(package)], stdout=PIPE, stderr=PIPE)
            pipout, piperror = pip.communicate()
            sys.stderr.write(pipout.decode('utf-8'))
            sys.stderr.write(piperror.decode('utf-8'))
    else:
        print("import {}".format(found))
