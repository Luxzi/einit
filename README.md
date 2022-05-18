# einit
**Initialize your projects with one command. Easy, Customizable, Flexable, Fast.**

v1.7-expiremental

## Installation

### Using the einit-bootstrapper (_Windows_) **Experimental**

Download the latest version from the releases and run it.

## Updating
Since this program is not a package you'll have to update it manually. This can be done by downloading the ``Makefile`` and running ``make uninstall`` then following the normal install instructions.

## Contributing
Create an issue or pull request.

## Usage
Run einit using the terminal in the directory you'd like to create your project in, you can also specifiy the name of a file in the ``/etc/einit`` folder to be used as a config file eg. ``einit cpp``. If you'd like to modify the way **einit** works edit its config file in ``/etc/einit/config.yaml``.

## (NEW) Plugins

Plugins allow you to easily extend the functionality of **einit** without having to edit the main source.

### Creating an einit plugin
Create a ``.py`` file at ``/etc/einit/plugins`` with your plugins name. Every plugin must have its metadata defined in its file, the metadata is set by setting variables, here is some example metadata:

```
  version = "1.0"
  author = "Luxzi"
```

The next step is creating our main function, this is defined as follows:

```
  def run():
    # Function code here
```

Now you have a basic plugin.

### Adding config options and using the API
To import the API add these import lines:

```
  import sys
  import yaml
  sys.path.append("/usr/local/bin/einit")
  import einit_globals as g
```

Next we define the config location as a variable:

```
  try:
     config = g.conf()
  except:
    print("PluginName: Plugin: ERROR: Could not find config file!")
    quit()
```

Now to setup the YAML parser:

```
  file = open(config, 'r')
  config = yaml.safe_load(file)
```

### Creating config options

Use ``if`` statements and ``for`` loops to define config options, following the **pyyaml** documentation: [PyYAML Docs](https://pyyaml.org/wiki/PyYAMLDocumentation)

## Config file

An example C++ config file is included as the default config.

### Multi-config support

By default running einit without any arguments will use the included ``config.yaml`` in ``/etc/einit`` but adding the filename (without extentsion) as an argument will try and locate the respective ``.yaml`` file, so for example you could have ``einit cpp`` setup your C++ development enviorment or anything really, but keep in mind that if your config is invalid it **will** cause errors.

## Required config file options

### Makefile Section
The ``makefile`` section in the config file defines the where to get the makefile and if the makefile should be grabbed.

### Tree section
The ``tree`` section contains the directories and directory trees that should be created.

Section rules:
- Folder numbers start at 0.
- Any numbered entry will be treated as a folder.
- Using a foward slash in between two of the folder names will create a tree with those folders eg. "bin/release" creates the bin folder then creates the release folder in it.
- Any enteries that are not numbers with be ignored eg. '1: "Folder"'

### Files section
Only numbered enteries are allowed, enteries start at 0.

Note: If you want to create a file in sub-directory that directory must exist, so make sure you add it to the tree in the ``config.yaml`` then use the folder name followed by a foward slash and then the file name.

### Test Compile section
This parameter defines wether you'd like a hello world program to automaticlly be compiled on project creation to test development tools.

Note: This requires index 0 of files in ``config.yaml`` to be ``main.cpp`` and the ``get`` parameter of ``makefile`` to be true.

## Optional config file options

There are no default optional config file options but plugins can create them.
