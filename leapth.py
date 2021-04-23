





#######################################################################################


import threading
import leap as fl
import os
import time


fl.datastorage()

  
if __name__ == "__main__":
    

    key=input("enter the key : ")
    value=int(input("enter the value for the key : "))
    timeout=int(input("enter the timeout(numeric) : "))



    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))
  
    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))



    # creating threads
    t1 = threading.Thread(target=fl.create,args=(key,value,timeout)) 
    time.sleep(2)
    t2 = threading.Thread(target=fl.read,args=(key,)) 
  
    # starting threads
    t1.start()
    t2.start()
    
    # wait until all threads finish
    t1.join()
    t2.join()




####################################################################################################