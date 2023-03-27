from tqdm import tqdm
import pyfiglet as pyg  
import zipfile
import sys


# pretty banner to unixIp  
res= pyg.figlet_format("Unix ZIP", font = "slant")   

print(res)
print("#"*5,"created by unixcoder","#"*5)

import zipfile

zip_file = input("Enter the name of the zip file: ")
dictionary_file = input("Enter the name of the dictionary file: ")

with open(dictionary_file, 'r') as f:
    passwords = f.readlines()

for password in passwords:
    password = password.strip('\n')
    try:
        with zipfile.ZipFile(zip_file) as zf:
            zf.extractall(pwd=password.encode())
            print(f"Password found: {password}")
            break
    except:
        pass


print("Thanks for Hacking 😋")

############################################
############################################
############################################
################created by coder############
###########################################
############################################
############################################
############################################
