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

# File path
path = '/Users/tarundeep/Desktop/Python_TDS/Python_Projects/Network_Application_5_Config_Mgmt_Email_Notification_For_Config_Changes/cfgfiles/' 

#Defining the device type for running netmiko. Netmiko has multi vendor support, so telling which OS we are using will enhance its capabilities
device_type = 'arista_eos'
 
#Defining the username and password for running netmiko
username = 'admin'
password = ''
 
#Defining the command to send to each device
command = 'show running'

#Connecting to the device via SSH, global_delay_factor is used to avoid timeout error in case of slow connections
session = ConnectHandler(device_type = device_type, ip = ip_smm353, username = username, password = password, global_delay_factor = 3)

#Entering enable mode
enable = session.send_command_expect("enable",expect_string = r".+")

#Sending the command and storing the output (running configuration)
output = session.send_command(command) # as show run command can take time so added timeout delay

#Defining the base file for comparison.
device_cfg_old = path + 'Base_Config'

#Writing the command output to a new file for today.
with open(path + ip_smm353 + '_' + datetime.date.today().isoformat(), 'w') as device_cfg_new:
    device_cfg_new.write(output + '\n')
 
#Extracting the differences between yesterday's and today's files in HTML format
#Compare the base files with today's config file line by line
with open(device_cfg_old, 'r') as old_file, open(path + ip_smm353 + '_' + datetime.date.today().isoformat(), 'r') as new_file:
    difference = difflib.HtmlDiff().make_file(fromlines = old_file.readlines(), tolines = new_file.readlines(), fromdesc = 'Yesterday', todesc = 'Today')

#Sending the differences via email
#Defining the e-mail parameters
fromaddr = 'pythontds@gmail.com'
toaddr = 'pythontds@gmail.com'
 
#More on MIME and multipart: https://en.wikipedia.org/wiki/MIME#Multipart_messages
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Daily Configuration Management Report'
msg.attach(MIMEText(difference, 'html'))
 
#Sending the email via Gmail's SMTP server on port 587
server = smtplib.SMTP('smtp.gmail.com', 587)
 
#SMTP connection is in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted.
server.starttls()
 
#Logging in to Gmail and sending the e-mail
# If face issues check https://stackoverflow.com/questions/73383458/login-authentication-failed-with-gmail-smtp-updated
server.login('pythontds', 'ggmazovvznltscyp')
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()