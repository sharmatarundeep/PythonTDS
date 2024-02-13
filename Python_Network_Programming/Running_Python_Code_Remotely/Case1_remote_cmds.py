# Case 1 - Running CLI commands via remote server. Create a script on your local PC and this script open a SSH session to a remote server like st101 and from this remote server you create a SSH session to the device and run commands
#Use jumpssh module for this functionality. To install jumpssh "pip3 install jumpssh"
from jumpssh import SSHSession

#create a remote server session 
server_session = SSHSession ("st101", "tarundeep", password="arista")

#create a switch session from server session
switch_session = server_session.get_remote_session("smm353", "admin", password="")

#Now try to execute a command from server to the switch and make sure it works
print(switch_session.get_cmd_output("show ip in br"))

#close the server session this will automatically close the switch session as switch session was created on server session
server_session.close()

