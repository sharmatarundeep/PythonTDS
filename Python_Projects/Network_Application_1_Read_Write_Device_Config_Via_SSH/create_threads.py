# Will be used to create multiple thread so that we can configure multiple devices in parallel
import threading
# import ssh_connection # for testing 

#this func will take care of creating multiple threads to ssh to all IPs/devices and push configuration
def create_threads(iplist, func): # here iplist is list taken from ip text file and func is the SSH function we defined earlier
    thread = [] # empty list to store the thread object for later execution 
    for ip in iplist:
        th = threading.Thread(target = func, args= (ip,)) # args is a tuple with single element and is needed for the ssh func
        th.start()
        thread.append(th)

    for th in thread:
        th.join() # make sure program completes all the threads of configuring DUTs and then  proceed with the program.

      
# create_threads(['172.30.190.25\n', '172.30.190.32\n', '172.30.190.31\n'], ssh_connection.ssh_connection) # just for testing
