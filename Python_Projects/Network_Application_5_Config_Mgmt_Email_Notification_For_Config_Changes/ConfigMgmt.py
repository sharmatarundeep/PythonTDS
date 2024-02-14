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
ip = '10.10.10.2'
 
#Defining the device type for running netmiko
device_type = 'arista_eos'
 
#Defining the username and password for running netmiko
username = 'admin'
password = 'python'
 
#Defining the command to send to each device
command = 'show running'