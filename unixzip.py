from tqdm import tqdm
import pyfiglet as pyg  
import zipfile
import sys


# pretty banner to unixIp  
res= pyg.figlet_format("Unix ZIP", font = "slant")   

print(res)
print("#"*5,"created by unixcoder","#"*5)


# the password list path you want to use
wordlist = sys.argv[2]
# the zip file you want to crack its password
zip_file = sys.argv[1]
# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
print("")
print("Thanks for Hacking 😋")

############################################
############################################
############################################
################created by coder############
###########################################
############################################
############################################
############################################
