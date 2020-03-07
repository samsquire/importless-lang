# importless-lang

a Python preprocessor that inserts import statements for you

See `example.py` - the file has no import statements

Global tokens are found `global_finder` from the sourcecode. Then mapped against `lookups.yml`

Run `./importless example` for a demonstration

# Adding imports to lookups

You have to add the package to `create-imports.py` and run `python3 create-imports.py` 
