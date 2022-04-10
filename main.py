"""Main Encryption File
"""


ALPHA = list("abcdefghijklmnopqrstuvwxyz")


#----------------------------------------------------------------
# imports
#----------------------------------------------------------------

import uuid
import random
import json
import os
import time


#----------------------------------------------------------------
# Sub-Functions
#----------------------------------------------------------------

def jtext(obj):
    """Takes json dict data and formats it in default json string

    Args:
        obj (json dict type object): The dict type object

    Returns:
        string: Formatted text
    """
    
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

def new_keys(num: int, file_name: str=False):
    """Generates new keys for use for encrypting text

    Args:
        num (int): The number of keys to generate
        file_name (str, optional): The file name to the keys generated. Defaults to False, generates universal unique id.

    Returns:
        dict: The keys in dict form
    """
    
    if file_name:
        file = open('keys/'+file_name+".json", 'w')
    else:
        file = open('keys/'+str(uuid.uuid1())+".json", 'w')
    
    # dicitionary to load
    keys = {}
    
    # Iterate through times and append each random key to the keys
    for n in range(num):
        a = ALPHA
        random.shuffle(a)

        key = {n+1: a}
        keys.update(key)
    
    # Convert to json string
    text = jtext(keys)
    
    # Write to output
    file.write(text)
    
    # Return the dict for further use
    return keys

def encrypt(text: str, keys):
    # makes it easier to iterate through
    text = list(text)
    
    # Change for each set of keys
    change = []
    
    for key in keys.values():
        holder = []
        
        # Iterate through text
        for letter in text:
            if letter.isalpha():
                index = ALPHA.index(letter)
                applied_index = key.index(index)
                holder.append(applied_index)
            else:
                holder.append(letter)

        change.append(holder)
    
    print(change[len(change)])
                

#----------------------------------------------------------------
# Main function
#----------------------------------------------------------------

def main():
    # Ask for new keys
    c = False
    while not c:
        Q_new_keys = input("Would you like to make new keys? (y/n) ")
        
        if Q_new_keys.lower() == "y":
            Q_new_keys = True
            c = True 
        if Q_new_keys.lower() == "n":
            Q_new_keys = False
            c = True

    if Q_new_keys:
        c = False
        while not c:
            Q_num = input("Number of new keys (1-25): ")
            
            try:
                Q_num = int(Q_num)
                
                if Q_num < 1 or Q_num > 25:
                    continue
                
                c = True
            except:
                pass
        
        Q_rename_file = input("Would you like to rename the file? (Defaults to uuid): ")
        
        if Q_rename_file == "":
            keys = new_keys(Q_num)
        else:
            keys = new_keys(Q_num, Q_rename_file)
            
    else:
        files = os.listdir(r'keys/')
        
        # Creation times
        creation_times = []
        
        for file in files:
            ti_c = os.path.getctime("keys/"+file)
            ti_c = time.ctime(ti_c)
            
            creation_times.append()
        
        max_time = max(creation_times)
        latest_file_index = creation_times.index(max_time)
        latest_file = files[latest_file_index]
        
        keys = json.load(r"keys/"+latest_file)
        
        print("\nLatest key file chosen\n")
        
    # Get text
    Q_text = input("Text (symbols like '!?,.' are ignored): ")
    
    encrypt(Q_text, keys)
    
if __name__ == "__main__":
    main()