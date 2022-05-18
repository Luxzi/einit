import os, sys

os.chdir(os.path.dirname(sys.argv[0]))
basepath = os.path.expanduser('~') + "\\AppData\\Local"
runpath = os.path.dirname(__file__)
confirm = input("WARNING: einit for windows is currently experimental, are you sure you want to continue? (y/N): ")

if(confirm != "y"):
    print("ERROR: User did not confirm install, exiting...")
    quit()

print("INFO: Attempting to clone remote repository...")
os.system("git clone https://github.com/Luxzi/einit -b windows")

if(os.path.isfile("einit") != True):
    print("ERROR: Unable to clone remote repository (Is git-scm installed?)")
    quit()

print("INFO: Repository cloned successfully...")
print("INFO: Creating directories...")

os.mkdir(basepath + "\\einit")
os.mkdir(basepath + "\\einit\\configs")
os.mkdir(basepath + "\\einit\\plugins")

if(os.path.isfile(basepath + "\\einit") == True and os.path.isfile(basepath + "\\einit\\configs") == True and os.path.isfile(basepath + "\\einit\\plugins") == True):
    print("INFO: Created directories")
else:
    print("ERROR: Could not create directories")
    quit()

print("INFO: Copying files...")

os.rename(runpath + "\\einit\\einit\\einit.py", basepath + "\\einit\\einit.py")
os.rename(runpath + "\\einit\\einit\\einit_globals.py", basepath + "\\einit\\einit_globals.py")
os.rename(runpath + "\\einit\\einit\\config.yaml", basepath + "\\einit\\configs\\config.yaml")
os.rename(runpath + "\\einit\\einit\\einit.bat", basepath + "\\einit\\einit.bat")

if(os.path.isfile(basepath == "\\einit\\einit.bat") == True and os.path.isfile(basepath + "\\einit\\einit.py") == True and os.path.isfile(basepath + "\\einit\\einit_globals.py") == True and os.path.isfile(basepath + "\\einit\\configs\\config.yaml") == True):
    print("INFO: Files copied...")
else:
    print("ERROR: Could not copy files...")
    quit()

print("INFO: Adding program to PATH...")

#os.system('setx path "%PATH%;' + basepath + '\\einit\\einit.bat"')

print("INFO: Added program to PATH")
print("INFO: Install complete, reload your terminal(s) to refresh their PATH variable and finish the install")
