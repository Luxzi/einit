import os
import sys
from os.path import exists
import yaml
import einit_globals as g
plugins = []
pbuffer = ""

for root, dirs, files in os.walk(g.path()):
    for file in files:
        pbuffer = ""
        for char in file:
            if char != ".":
                pbuffer += char
            else:
                break
        plugins.append(pbuffer)

del pbuffer

if os.path.exists(g.path() + "/__pycache__") == True:
    for i in plugins:
        x = 0
        if x != 1:
            p = x - 1
        else:
            p = 1
        if plugins[p] == plugins[x]:
            plugins.pop(x)
        x += 1

file = open(g.conf(), 'r')
config = yaml.safe_load(file)
trees = []

for i in range(0, len(config['tree'])):
    trees.append(config['tree'][i])

if config['makefile']['get'] == True:
    os.system("curl " + config['makefile']['link'] + " > Makefile")
    print("Makefile created")
else:
    print("Skipping makefile download, get is false")

for i in range(0, len(trees)):
	dirName = str(trees[i])

	try:
		os.makedirs(dirName)
		print("Directory " , dirName ,  " created ") 
	except FileExistsError:
		print("Directory " , dirName ,  " already exists")

for i in range(0, len(config['files'])):
    print("File " + config['files'][i] + " created")
    os.system("touch " + config['files'][i])

for i in range(0, len(config['commands'])):
    os.system(config['commands'][i])

print("\nPlugins:\n")
sys.path.append(g.path())
for name in plugins:
    plugin = __import__(name)
    version = plugin.version
    author = plugin.author
    print(name + " - " + version + " by " + author)
    plugin.run()