import nmap
import pprint # for more pretty print output

while True:
    #User menu
    print("""\nWhat do you want to do?\n
                1 - Get detailed info about a device
                2 - Scan the network for open ports
                e - Exit the application""")

    user_input = input("\nEnter your option: ")

    #Handling user options
    if user_input == "1":
        #Initializing the port scanner
        mynmap = nmap.PortScanner()

        #Asking the user for the IP address to scan
        ip = input("\nPlease enter the IP address to scan: ")

        print("\nThis may take a couple of minutes...\n")

        #Scanning the device (output is in dictionary format)
        scan = mynmap.scan(ip, '1-1024', '-v -sS -sV -O -A -e ens3')
        #pprint(scan)

        #Parsing the relevant information from the scan result
        #Header containing the IP address
        print("\n= = = = = = = HOST {} = = = = = = =".format(ip))

        print("\n\nGENERAL INFO")

        #MAC address
        try:
            mac = scan['scan'][ip]['addresses']['mac']
            print("\n-> MAC address: {}".format(mac))
        except KeyError:
            pass

        #Operating system
        os = scan['scan'][ip]['osmatch'][0]['name']
        print("-> Operating system: {}".format(os))

        #Device uptime
        uptime = scan['scan'][ip]['uptime']['lastboot']
        print("-> Device uptime: {}".format(uptime))

        #Port states
        print("\n\nPORTS\n")

        for port in list(scan['scan'][ip]['tcp'].items()):
            print("-> {} | {} | {}".format(port[0], port[1]['name'], port[1]['state']))

        print("\n\nOTHER INFO\n")

        #NMAP command used for scanning
        print("-> NMAP command: {}".format(scan['nmap']['command_line']))

        #NMAP version
        version = str(mynmap.nmap_version()[0]) + "." + str(mynmap.nmap_version()[1])
        print("-> NMAP version: {}".format(version))

        #Time elapsed
        print("-> Time elapsed: {}".format(scan['nmap']['scanstats']['elapsed'] + "seconds"))

        #Timestamp
        print("-> Time of scan: {}".format(scan['nmap']['scanstats']['timestr']))
        print("\n\n")

        continue

    elif user_input == "2":
        #Initializing the port scanner
        mynmap = nmap.PortScanner()

        print("\nThis may take a couple of minutes...\n")

        #Scanning the device
        scan = mynmap.scan(ports = '1-1024', arguments = '-sS -e ens3 -iL /home/osboxes/Apps/ip.txt')
        #pprint(scan)

        for device in scan['scan']:
            print("\nPorts open on {}:".format(device))
            for port in scan['scan'][device]['tcp'].items():
                if port[1]['state'] == 'open':
                    print("-->" + str(port[0]) + "|" + port[1]['name'])

        continue

    elif user_input == "e":
        print('\nExiting program...\n')
        break

    else:
        print("\nInvalid input. Try again!\n")

        continue

#End of program
