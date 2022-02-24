import os
menu_options = {
    '1': 'Update and/or Upgrade OS (packages)',
    '2': 'Install Main Modules',
    '3': 'Install Additional Modules (Strongly Recommended)',
    '4': 'Site Configurator v1.0',
    '5': 'DB Configurator + Site Preparator 2',
    '0': 'Exit',
}

def print_menu():
    print("===================================================")
    print("++                                               ++")
    print("++                                               ++")
    print("++    Welcome to Main Installation Manager       ++")
    print("++                                               ++")
    print("++                V. 1.0.                        ++")
    print("++                                               ++")
    print("===================================================")
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )   
#OS_SCE = Single Command Execution 
def OS_SCE(p_command):
    err = os.system(p_command)
    if err !=0 :
        return err
    return None
#OS_MCE = Multiple Command Execution 

def OS_MCE(p_list_commands):
    for _command in p_list_commands:
        err = os.system(_command)
        if err != 0 :
            return err
    return None    
def OS_Update(p_unity):
    __update= "apt update -y"
    __upgrade= "apt upgrade -y"
    __all = ["apt update -y",
             "apt upgrade -y",]

    if(p_unity == "UP"):
        OS_SCE(__update)
    elif(p_unity == "UPG"):
        OS_SCE(__upgrade)
    elif(p_unity == "ALL"):
        OS_MCE(__all)
    else:
        print("Action Aborted")
        os.system("clear")
    return OS_SCE
def MainModules(p_choice, p_extras):
    
    if (p_choice == "C" and p_extras == "Y"):
        print("Running Complete Installation Sequence")
        __complete_installation = [ "apt install apache2 -y",
                                    "apt install php7.4-common -y",
                                    "apt install mysql-client -y",
                                    "apt install mysql-server -y",
                                    "apt install ghostscript php7.4-pspell php7.4-curl php7.4-gd php7.4-intl php7.4-mysql php7.4-xml php7.4-xmlprc php7.4-xlmrpc php7.4-ldap php7.4-zip php7.4-soap php7.4-mbstring",
                                    ]
        OS_MCE(__complete_installation)
    elif (p_choice == "PW" and p_extras == "Y"):
        print("Running Partial Installation (Web-only) Sequence")
        __partial_installation_web = ["apt install apache2 -y",
                                      "apt install php7.4-common -y",
                                      "apt install ghostscript php7.4-pspell php7.4-curl php7.4-gd php7.4-intl php7.4-mysql php7.4-xml php7.4-xmlprc php7.4-xlmrpc php7.4-ldap php7.4-zip php7.4-soap php7.4-mbstring"
                                     ]
        OS_MCE(__partial_installation_web)
    elif (p_choice == "PDB" and p_extras == "N"):
        print("Running Partial Installation (DB-only) Sequence")
        __partial_installation_db = ["apt install mysql-client -y",
                                     "apt install mysql-server -y",]
        OS_MCE(__partial_installation_db)
    else:
        os.system("clear")
        print("Action Aborted...")
def AdditionalModules():
   
    yeah = str(input("Install Additional Site Modules (Y/N) (Strongly Recommended!): ")).upper()
    if(yeah == "Y" or yeah == "YES"):
        __php_modules = [ "apt install graphviz aspell php8.0-pspell php8.0-curl php8.0-gd php8.0-intl php8.0-mysql php8.0-xml php8.0-ldap" ]
        OS_MCE(__php_modules)
    else:
        print("Action Aborted...")
        os.system("clear")
def SiteConfigurator():

    __moovable_sed = [  "echo 'Preparing Environment...'",
                        "git clone git://git.moodle.org/moodle.git",
                        "echo 'Moving Branch to the Webroot...'",
                        "sleep 2",
                        "mv -v moodle /var/www/html/",
                        "echo 'Generating moodledata directory...'",
                        "sleep 3"
                        "mkdir -p /etc/moodledata",
                        "echo 'Writing permissions to |/etc/moodledata|...'",
                        "chown -R www-data /etc/moodledata",
                        "chmod -R 0777 /etc/moodledata",
                        "chmod -R 0755 /var/www/html/moodle",
                        "echo 'Site Structure configuration is complete!'",
                        "sleep 1"
                        "echo 'Please Configure your DB before finished the installation'",
                        "sleep 5",                    
                        ]  
    OS_MCE(__moovable_sed)
def DockerConfigurator():
    print("If you don't have MySQL Server installed on your system use Docker to prepare and configure the Server")
    __run_file = ["echo 'Preparing Environment...'",
               "sleep 5",
               "echo 'Fetching mysql configuration file...'",
               "sleep 5",
               "echo 'Executing |mysql.yaml|...'",
               "docker-compose -f mysql.yaml up -d",
               "docker exec -it mysql_moodle /bin/bash",
               "cd /etc/mysql/mysql.conf.d",
               "echo 'default_storage_engine = innodb' >> mysqld.conf",
               "echo 'innodb_file_per_table = 1' >> mysqld.conf",
               "echo 'innodb_file_format = Barracuda' >> mysqld.conf",
               "exit",
               "docker restart mysql_moodle"]
    OS_MCE(__run_file)
if __name__=='__main__':
    while(True):
        print_menu()

        option = ''
        try:
            option = str(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == '1':
            unity = input(("Type | UP | to update, | UPG | to upgrade, | ALL | to update and upgrade the OS or | X | to Abort this Action: ")).upper()
            OS_Update(unity)
        elif option == '2':
            print("To run semi-automatic installation script type \n")
            choice = input(("| C | for Complete, | PW | for Partial Web, | PDB | for Partial DB Installation or | X | to Abort the Installation: ")).upper()
            modules = input(("Type Y or N to install extra PHP modules for you Moodle: ")).upper()
            MainModules(choice, modules)
        elif option == '3':
            AdditionalModules()
        elif option == '4':
            SiteConfigurator()
        elif option == '5':
            DockerConfigurator()    
        elif option == '0':
            exit()
        else:
            print('Invalid option. Please enter a number between 0 and 6.')

