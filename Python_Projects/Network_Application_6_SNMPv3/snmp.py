#Importing the necessary module
# If needed pip3 install easysnmp
from easysnmp import Session

def snmpv3():
	#Asking the user for input
	ip = input('\nEnter the device IP address: ')

	oid = input('\nEnter the OID or MIB name to work on: ')

	#Opening the SNMPv3 session to the device
	session = Session(hostname = ip, version = 3, security_level = "auth_with_privacy", security_username = "tarundeep", auth_protocol = "SHA", auth_password = "shapass1234", privacy_protocol = "AES", privacy_password = "aespass1234")

	return oid, session

while True:
	#User input
	print('\nChoose the SNMP operation you want to perform:\n\ng - SNMP GET\nw - SNMP WALK\ns - SNMP SET\ne - Exit program')

	user_choice = input('\nEnter your choice: ')
    
    #SNMP GET
	if user_choice == 'g':
		snmp = snmpv3()
		oid = snmp[0]
		session = snmp[1]

		#Performing SNMP GET
		snmp_get = session.get(oid)

		#Getting the value returned by the device
		result = snmp_get.value

		#Printing the value
		print('\nThe result of SNMP GET on {} is:'.format(oid))
		print('\n' + result + '\n')

		continue
    
    #SNMP WALK
	elif user_choice == 'w':
		snmp = snmpv3()
		oid = snmp[0]
		session = snmp[1]

		#Performing SNMP WALK
		snmp_walk = session.walk(oid)

		#Printing the result
		print('\nThe result of SNMP WALK on {} is:'.format(oid))

		for obj in snmp_walk:
			result = obj.value
			print('\n' + result)

		continue

	#SNMP SET (bug in easysnmp)
	#https://github.com/kamakazikamikaze/easysnmp/issues/108
	elif user_choice == "s":
		snmp = snmpv3()
		oid = snmp[0]
		session = snmp[1]

		#Performing SNMP SET
		value = input("\nEnter the value for the object: ")

		snmp_set = session.set(oid, value)

		print("\nDone. Please check device configuration.")

		continue

	elif user_choice == 'e':
		print('\nExiting program...\n')

		break

	else:
		print('\nInvalid input. Try again!\n')

		continue

#End Of Program