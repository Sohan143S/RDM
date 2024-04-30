import os, sys
os.system("git pull")
try:
    __import__("sex_sn").menu()
except Exception as e:
    exit(str(e)) 
