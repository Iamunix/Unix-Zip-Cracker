#!/use/bin/evn python3
# https://github.com/Iamunix
# Author - iamunix

import sys
import zipfile
from tqdm import tqdm

# pretty banner to unixZIP Cracker

print("""\033[1;96m
 _   _       _        ______         _
| | | |_ __ (_)_  __ |__  (_)_ __   | |
| | | | '_ \| \ \/ /   / /| | '_ \  | |
| |_| | | | | |>  <   / /_| | |_) | |_|
 \___/|_| |_|_/_/\_\ /____|_| .__/  (_)
                            |_| v1.0
------------created by unixcoder------------
 \033[0;0m""")

zip_file = input("Enter the name of the zip file: ")
dictionary_file = input("Enter the name of worldlist: ")

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

print("Happy Hacking🦈")

























############################################
############################################
############################################
################created by coder############
###########################################
############################################
############################################
############################################
