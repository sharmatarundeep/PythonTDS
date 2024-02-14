* Python Network Application # 4 - Config Management on the devices and sending email notification about the config changes. 
* Overview - We will login to a device save the running config and next day again save the running config, later compare the latest running config with yesterday and send email to the user in HTML format about the config changes. We can also schedule a job to run this application periodically.


Modules used 
* datetime (for time stamping anything) 
* difflib (Compare and find the difference)  
* smtplib (To create a SMTP (Simple Mail Transfer Protocol) client object that can be used to send email)  
* email.mime.multipart (To create the email content)  
* email.mime.text (To create the email content)  
* netmiko (Like paramiko used for SSH)  

<br>
Author - Tarundeep Sharma
