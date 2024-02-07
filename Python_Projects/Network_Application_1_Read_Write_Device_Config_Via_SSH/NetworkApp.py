# Final program, putting everything together and run this to execute the functionality we developed for this project
# Remember create_thread function would need list of IP address and ssh_connetion function
import sys
from ip_addr_valid import ip_addr_valid
from ip_file_valid import ip_file_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads

# Saving the list of IP addresses in a variable 
ip_list = ip_file_valid()
print ("\n\nThese are the devices we are about to configure :\n", ip_list)

# Quickly verify the validity of each IP address 
try:
    ip_addr_valid(ip_list)
except KeyboardInterrupt: # incase keyboard interupt happended
    print("Program was aborted by user")
    sys.exit

# Quickly verify the reachability of each IP address 
try:
    ip_reach(ip_list)
except KeyboardInterrupt: # incase keyboard interupt happended
    print("Program was aborted by user")
    sys.exit

# Now call create_thread func to start executing commands on all devices simultaneously
create_threads(ip_list, ssh_connection)

# Now suppose you want to extract NTP server's ip address for all the devices from "show ntp status". 
# For this lets add functionality to the ssh_connection file as that is where we are running these commands
# Later when we will call ssh_connection function in this file, NTP server ip will be extracted for all the devices in multi threading
'''sk251.08:09:28(config)#show ntp status
synchronised to NTP server (10.90.20.122) at stratum 3
   time correct to within 38 ms
   polling server every 1024 s

sk251.08:09:29(config)#'''

