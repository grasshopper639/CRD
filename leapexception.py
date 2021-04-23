###########################################################################

# the error messages 

def duplicate(key):   # thrown when there exists a duplicate key
	message = "key "+key + " already exists, create another"
	return message

def invalid(key):     # throws when the string is numeric or alphanumeric
	message = key + " name should be string"
	return message

def memorylimit(key):  # throws when the size limit exceeds
	message = "memory limit exceeded"
	return message

def keynot(key):    # throws when it doesn't exits
	message = "given key "+key+" doesn't exists, please enter a valid key"
	return message

def timetolive(key):  # throws the time to live
	message = "time to live for the "+key+" has expired"
	return message

def deletekey(key): # throws it is deleted
	message = "key "+key+" is deleted!!"
	return message

####################################################################################S
