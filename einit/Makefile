install:
# Create einit directory in etc then copy the default config and plugins folder into it
	sudo mkdir -p /etc/einit
	sudo cp config.yaml /etc/einit/config.yaml
	sudo cp -r plugins /etc/einit
# Create einit in /usr/local/bin then move program files into /usr/local/bin/einit and create bash command alias
	sudo mkdir -p /usr/local/bin/einit
	sudo cp einit.py /usr/local/bin/einit/einit.py
	sudo cp einit_globals.py /usr/local/bin/einit/einit_globals.py
	echo "alias einit='python3 /usr/local/bin/einit/einit.py'" >> ~/.bashrc
	
uninstall:
# Remove all program files, plugins, and configs
	sudo rm -r /etc/einit
	sudo rm /usr/local/bin/einit/einit.py
	sudo rm /usr/local/bin/einit/einit_globals.py