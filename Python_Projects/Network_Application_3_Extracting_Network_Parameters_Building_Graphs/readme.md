* Python Network Application # 3 - Extracting Network Parameters & Building Graphs.
* Overview - Connect to a network device using ssh, check CPU utilization periodically until interrupted to build a database in a text file and later build a graph on CPU utilization. Also, our graph will dynamically update itself in real time.  
* To run the application, open 2 terminal and run NetworkApp.py from one and graph.py from another terminal.
* NetworkApp.py will publish the CPU utilization data in text file every 10 seconds.
* Graph.py will continue to plot graph by polling data every 10 seconds in real time.

Modules used 
* os.path (for check if file exist or not)
* sys (for exiting the program in case of error sys dot exit())
* paramiko (used for SSH and networking remote connectivity)
* subprocess (to send ping command)
* matplotlib (to draw graphs)


<br>
Author - Tarundeep Sharma
