echo "Initializing einit installer..."

if [ `whoami` != root ]; then
    echo "ERROR: This install script requires elevated permissions to execute correctly, please run it using sudo, doas or some other privilege escalation utility."
    exit
fi

if [ `uname -o` != "GNU/Linux" ]; then
    echo "ERROR: This script is only compatable with GNU/Linux systems, and is being run on a non-GNU/Linux system."
    exit
fi

if [ `where git` = "git not found" ]; then 
    echo "ERROR: 'git' is not installed but is required to run this script."
    exit
fi

if [ `where pip` = "pip not found" ]; then
    echo "ERROR: 'pip' is not installed but is required to run this script."
    exit
fi

git clone https://github.com/Luxzi/einit

mkdir /usr/local/bin/einit
mkdir /usr/share/doc/einit
mkdir /etc/einit
mkdir /etc/einit/plugins

mv einit/einit/einit.py /usr/local/bin/einit/einit.py
mv einit/einit/einit_globals.py /usr/local/bin/einit/einit_globals.py
mv einit/einit/config.yaml /etc/einit/config.yaml
mv einit/README.md /usr/share/doc/einit/README.md

pip install pyyaml

echo "INFO: Install Complete."
echo "INFO: Make sure to reload your terminal(s) to update their alias and finish the install."
