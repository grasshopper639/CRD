###################################################################

import threading
from threading import *
import time
from leapexception import *
import os
import json
_db_lock = Lock() # the threading will not get pollute
hashfile={} #hashfile is the dictionary


file_limit = 1024*1024*1024 #limit on the file size i.e. 1GB, in create function
value_limit = 16*1024*1024 #limit for the object i.e 16kb
filename = "" #to store the filename, default is "database.json"

###################################################################

#function to create or load the json file

def datastorage():
    global filename
    global hashfile
    value = input("enter the file path :: 1.yes 0.the defaut ")
    if value == "1":
        filename = input("enter the filename : ")
    else:
        filename = 'atabase.json' #filename default json file 
    with open(filename,'w') as ds:
        if os.stat(filename).st_size == 0:
            st='{}'
            ds.write(st)
    with open(filename,'r') as ds:
        data_load = json.load(ds)            
        temp=data_load
        print("loaded data file")
        print(temp)
        d=temp

#############################################################################

# to verify whether the key is string or alphanuric, and less
# than 32 chars, this function is also used in leaptry.py file to verify the 
# entered key is valid or not

def verify(key):
    
    if len(key) > 32:
        return False
    if len(key)<=32: # the key should be less than 32 chars
        if key.isalpha():
            return True
        else:
            return False
    

##############################################################################

# create function
# this function checks for duplicate, invalid, and memory limit key

def create(key,value,timeout=0):

    #print("ID of process running task 1: {}".format(os.getpid()))  # to get ID of current process, uncoment during 
                                                                   # multithreading demonstration, while running leapth.py
    if verify(key) == True: #to verify whether the key is string or alphanuric, and less
                            # than 32 chars
        global filename
        global hashfile
        if key in hashfile:
            print(duplicate(key)) 
        else:
            if(type(key) == str):
                if len(hashfile)<file_limit and value<=value_limit: 
                    print()
                    print("#### key value created ###")
                    print()
                    if timeout==0:
                        l=[value,timeout]
                    else:
                        l=[value,time.time()+timeout]
                    if len(key)<=32: 
                        hashfile[key]=l
                        with open(filename,'w') as ds:
                            json.dump(hashfile,ds)
                    else:
                        print(memorylimit(key))
                else:
                    print(memorylimit(key))
            else:
                print(invalid(key))
    else:
        print(memorylimit(key))

################################################################################

# read function

def read(key):
    #print("ID of process running task 2: {}".format(os.getpid())) # to get ID of current process, uncoment during 
                                                                   # multithreading demonstration, while running leapth.py
    if verify(key) == True: # to verify whether the key is string or alphanuric, and less
                            # than 32 chars

        global filename
        global hashfile
        if key not in hashfile:  # checks if the key is present or not, if not 
            print(keynot(key))   # prints gives the error message
        else:
            if hashfile[key][1]!=0:          # checks the second value which is time to live value is 0 or not
                if time.time()<hashfile[key][1]: # comparint the present time with given time to live 
                    value =str(key)+":"+str(hashfile[key][0]) # storing the value as json object
                    print(value)
                else:
                    print(timetolive(key)) 
            else:
                value=str(key)+":"+str(hashfile[key][0])
                print(value)
    else:
        print(memorylimit(key))

#######################################################################################

# delete function
def delete(key):

    if verify(key) == True: # to verify whether the key is string or alphanuric, and less
                            # than 32 chars
        global filename
        global hashfile
        if key not in hashfile: # checking iif the key is present in the hashfile
            print(keynot(key)) 
        else:
            if hashfile[key][1]!=0:               # checks the second value which is time to live value is 0 or not
                if time.time()<hashfile[key][1]: # compare it with the present time with given time to live 
                    del hashfile[key]
                    with open(filename,"r") as ds:
                        data = json.load(ds)
                        if key in data:
                            del data[key]

                    print(deletekey(key))
                else:
                    print(timetolive(key)) 
            else:
                del hashfile[key]
                print(deletekey(key))
    else:
        print(memorylimit(key))



###################################################################################################
