import threading 
import time

done = False # Just a variable to be used later to control a loop

# Target function - just sleep 1 second and printer counter value, this is like infinite loop until done is True
def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print (counter)

# Now support we don't use multi threading , it will become infine loop
#worker() # call worker function
#input("Press Enter to exit") #these 2 statements will not be executed as worker will never stop..
#done = True #these 2 statements will not be executed as worker will never stop..

# Lets use multithreading 
t1 = threading.Thread(target=worker) # create a thread object with worker as target function
t1.start() # start the t1 thread , now worker will run in seperate thread

input("Press Enter to exit") # now if you run the program thread t1 will start seperately and main func will resume
done = True # once you press enter this will execute, leading to while loop to end in worker function

