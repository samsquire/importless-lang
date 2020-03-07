import yaml
import sys
import global_finder

found_globals, tree = global_finder.find_globals(sys.stdin)

data = yaml.safe_load(open("lookups.yml").read())
for found in found_globals:
    if found in ["print", "__name__"]:
        continue
    if found in data:
        package = data[found]["package"]
        print("from {} import {}".format(package, found))
    else:
        print("import {}".format(found))

