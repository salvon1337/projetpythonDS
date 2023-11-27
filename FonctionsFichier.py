import re
import random
import string
import maskpass
import os
import hashlib


#retourne le length du fichier
def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    f.closed
    return i + 1

#check if fichier is empty
def file_is_empty(path):
    return os.stat(path).st_size==0


# the existance of email in the file
def existemail(x , email1) :
    i = 0
    for line in x :
            if (i != 0):
                    testupdate = re.split('([a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,}))',line)
                    if (email1 == testupdate[1]):
                        return testupdate
            i+=1
    return 0

# the existance of password in the file
def existpass(x , pass1) :
    i = 0
    print(pass1)
    for line in x :
            if (i != 0):
                    testupdate = re.split('([a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,}))',line)
                    print(testupdate[3])
                    if (pass1 == testupdate[3]):
                        return testupdate
            i+=1
    return 0