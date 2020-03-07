#!/usr/bin/env python3
import yaml
def add_imports(data, name, library):
    offerings = dir(library)
    for offering in offerings:
        data[offering] = {"package": name}

data = {}

import subprocess
import flask
add_imports(data, "subprocess", subprocess)
add_imports(data, "flask", flask)

open("lookups.yml", "w").write(yaml.dump(data))

