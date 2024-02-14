# To install netmiko , do the following
'''sudo apt-get update && sudo apt-get install libssl-dev
sudo pip3 install netmiko'''

#Importing the necessary modules
import difflib
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from netmiko import ConnectHandler
 
#Defining the device to monitor
ip_smm353 = '172.30.190.31'
 
#Defining the device type for running netmiko. Netmiko has multi vendor support, so telling which OS we are using will enhance its capabilities
device_type = 'arista_eos'
 
#Defining the username and password for running netmiko
username = 'admin'
password = ''
 
#Defining the command to send to each device
command = 'show running'

#Connecting to the device via SSH, global_delay_factor is used to avoid timeout error in case of slow connections
session = ConnectHandler(device_type = device_type, ip = ip, username = username, password = password, global_delay_factor = 3)
 
#Entering enable mode
enable = session.enable()
 
#Sending the command and storing the output (running configuration)
output = session.send_command(command)
