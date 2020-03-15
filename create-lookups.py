#!/usr/bin/env python3
import yaml
def add_imports(data, name, library, pip=None):
    offerings = dir(library)
    for offering in offerings:
        data[offering] = {"package": name}
        if pip:
            data[offering]["pip"] = pip

data = {}

import subprocess
import flask
add_imports(data, "subprocess", subprocess)
add_imports(data, "flask", flask, "flask")

open("lookups.yml", "w").write(yaml.dump(data))

