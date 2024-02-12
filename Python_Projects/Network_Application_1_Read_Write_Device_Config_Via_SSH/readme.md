* Python Network Application # 1 - Created this tool/program/application to read and write configurations to a device via SSH
* There are 3 text files for user input of - IP addresses of devices, username/password to access, configurations to be sent to devices
* There are various pythons files to perform small operations like - check all 3 text file exist or not, ip addressed provided are valid or not, devices are reachable or not, establish ssh to one device at a time and run commands, creating multiple threads..
* At last we have the main program file "NetworkApp.py". This is basically putting everything together and run this to execute the functionality we developed for this project

Modules used 
* os.path (for check if file exist or not)
* sys (for exiting the program in case of error sys dot exit())
* paramiko (used for SSH and networking remote connectivity)


<br>
Author - Tarundeep Sharma
