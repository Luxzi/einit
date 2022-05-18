#include <iostream>
#include <filesystem>
#include <string>
#include <sys/stat.h>
#include <cstring>

namespace fs = std::filesystem;

int main() {
    std::string dirname = fs::temp_directory_path().string() + "einit";
    std::string clonecomstr = "git clone https://github.com/Luxzi/einit.git -b windows " + dirname;
    
    char * clonecom;
    strcpy(clonecom, clonecomstr.c_str());
    char * user = getenv("username");
    char * uconst = "C:/Users/";

    std::string maindir = std::string(uconst) + std::string(user) + "/AppData/Local/einit";
    std::string configdir = std::string(uconst) + std::string(user) + "/AppData/Local/einit/configs";
    std::string plugindir = std::string(uconst) + std::string(user) + "/AppData/Local/einit/plugins";

    std::string mainfile = "move " + dirname + "einit/einit/einit.py " + dirname;
    std::string globalsfile = "move " + dirname + "einit/einit/einit_globals.py " + dirname;
    std::string dconfile = "move " + dirname + "einit/einit/config.yaml " + dirname + "/configs";
    char * mainfile_c;
    char * globalsfile_c;
    char * dconfile_c;
    strcpy(mainfile_c, mainfile.c_str());
    strcpy(globalsfile_c, globalsfile.c_str());
    strcpy(dconfile_c, dconfile.c_str());

    std::string confirmation_prompt;

    std::cout << "WARNING: einit for windows is currently expiremental, are you sure you want to continue (y/N): ";
    std::cin >> confirmation_prompt;

    if (confirmation_prompt != "y") {
        printf("ERROR: User did not confirm installation, exiting...");
        return -1;
    }

    printf("\nINFO: Attempting to clone einit repo...");
    system(clonecom);    

    if(!user) {
        printf("\nERROR: Couldn't get current user, exiting...");
    }

    if (!fs::exists(dirname)) {
        printf("\nERROR: Unable to clone einit repo (Is git-scm installed?)");
        return -2;
    }

    printf("\nINFO: einit repo cloned successfully.");
    printf("\nINFO: Creating directorys...");

    fs::current_path(fs::temp_directory_path());
    fs::create_directories(maindir);
    fs::create_directories(configdir);
    fs::create_directories(plugindir);

    if (fs::exists(maindir) && fs::exists(configdir) && fs::exists(plugindir)) {
        printf("\nINFO: Successfully created directories...");
    } else {
        printf("\nERROR: Failed to create some directories exiting...");
        return -3;
    }

    printf("\nINFO: Copying files...");

    /*fs::copy_file(mainfile, std::string(uconst) + std::string(user) + "/AppData/Local/einit");
    fs::copy_file(globalsfile, std::string(uconst) + std::string(user) + "/AppData/Local/einit");
    fs::copy_file(dconfile, std::string(uconst) + std::string(user) + "/AppData/Local/einit/configs");*/
    system(mainfile_c);
    system(globalsfile_c);
    system(dconfile_c);

    if (fs::exists(maindir + "einit.py") && fs::exists(maindir + "einit_globals.py") && fs::exists(configdir + "config.yaml")) {
        printf("\nINFO: Successfully copied files...");
    } else {
        printf("\nERROR: Failed to copy some files exiting...");
        return -3;
    }

    printf("\nINFO: Adding path variable...");

    // Add PATH stuff here

}