# importless-lang

a Python preprocessor that inserts import statements for you

* See `example.py` - the Python file has no import statements. But you can run it with `./importless example.py`

# How it works

Global tokens are searched with `global_finder` using the sourcecode's AST. Then looked up in `lookups.yml` to see what needs to be imported for which symbol.

# Adding imports to lookups

You have to add the package to `create-imports.py` and run `python3 create-imports.py`

