##############################################################################################

import leap as fl
import time
from threading import *



fl.datastorage() # initiates this function to create or load the datafile
            


while(True):


    value=input("want to perform create, read, delete:: 1.yes, 0.no ")
    if value=="0":
        break
    x=int(input("1.create 2.read 3.delete :: enter(1/2/3): "))


    if x==1:
        key=input("enter the key : ")

        value=int(input("enter the value for the key : "))
        timeout=int(input("enter the timeout(numeric) : "))
        
        # target the function to be executed 
        # args is the argument
        t1=Thread(target=fl.create,args=(key,value,timeout)) 
        t1.start()
                                         
      
            
    elif x==2:
        key=input("enter the key which you want to read : ")
        # target the function to be executed 
        # args is the argument
        t3=Thread(target=fl.read,args=(key,)) 
        t3.start()
        time.sleep(0)


    elif x==3:
        key=input("enter the key which you want to delete : ")
        # target the function to be executed 
        # args is the argument
        t4=Thread(target=fl.delete,args=(key,)) 
        t4.start() 
        time.sleep(0)
        
    else:
        print("perform again")




########################################################################################################