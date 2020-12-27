import threading
import time

data = {}

# Create operation
# Syntax "create(key_name,value,timeout_value)" or "create(key_name,value)


def create(key, value, timeout=0):
    if key in data:
        print("Error : Key already exists!")
    else:
        if(key.isalpha()):
            if len(data) < (1024*1020*1024) and value <= (16*1024*1024):
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time()+timeout]
                if len(key) <= 32:
                    data[key] = l
            else:
                print("Error: Memory limit exceeded! ")
        else:
            print("Error: Invalid key! Key must contain only Alphabets!")


# Read operation
# Syntax "read(key_name)"

def read(key):
    if key not in data:
        print("Error: Given key does not exist in Database. Please enter a valid key!")
    else:
        b = data[key]
        if b[1] != 0:
            if time.time() < b[1]:
                value = str(key)+":"+str(b[0])
                return value
            else:
                print("error: Time-To-Live of", key, "has expired")
        else:
            value = str(key)+":"+str(b[0])
            return value


# Delete operation
# Syntax "delete(key_name)"

def delete(key):
    if key not in data:
        print("Error : Given key does not exist in Database.Please enter a valid key")
    else:
        b = data[key]
        if b[1] != 0:
            if time.time() < b[1]:
                del data[key]
                print("Key is successfully deleted")
            else:
                print("Error : Time-To-Live of", key, "has expired")
        else:
            del data[key]
            print("Key is successfully deleted")


# Update/Edit operation
# Syntax "update(key_name,new_value)"

def update(key, value):
    b = data[key]
    if b[1] != 0:
        if time.time() < b[1]:
            if key not in data:
                print(
                    "Error : Given key does not exist in Database.Please enter a valid key")
            else:
                new = []
                new.append(value)
                new.append(b[1])
                data[key] = new
        else:
            print("Error : Time-To-Live of", key, "has expired")
    else:
        if key not in data:
            print("Error : Given key does not exist in Database.Please enter a valid key")
        else:
            new = []
            new.append(value)
            new.append(b[1])
            data[key] = new