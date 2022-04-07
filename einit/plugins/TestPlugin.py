# Plugin Metadata
version = "1.0"
author = "Luxzi"

import yaml
import sys
sys.path.append("/usr/local/bin/einit")
import einit_globals as g

def run():
    try:
        config = g.conf()
    except:
        print("TestPlugin: Plugin: ERROR: Could not open config file!")
        quit()

    file = open(config, 'r')
    config = yaml.safe_load(file)

    try:
        if config['makefile'] != None and config['tree'] != None and config['files'] != None and config['commands'] != None:
            print("TestPlugin: Plugin: Info: Plugins are working, Full access to config file!")
    except:
        None
    