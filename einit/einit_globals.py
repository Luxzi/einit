import sys

def conf():
    confpath = "/etc/einit/"

    try:
        conf = sys.argv[1]
        config = confpath + conf + ".yaml"
    except:
        config = confpath + "config.yaml"

    return config
         
def path():
    path =r'/etc/einit/plugins'
    return path