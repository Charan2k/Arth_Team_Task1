
import os
import getpass
from docker import docker
from hadoop import hadoop
from webserver import webserver
from partition import partition
from lvm import lvm
import aws

print("------------------Welcome to Automation of Different Technologies Menu------------------")

print("\t\t\t--------------------------------------")

passwd = getpass.getpass("Enter your password: ")

if passwd != "toor":
   print("password is incorrect....")
   exit()

while(True):
    print("""\n\n------------------MENU------------------
 Press  1 : For Docker
 Press  2 : For Hadoop
 Press  3 : For aws 
 Press  4 : For Partition 
 Press  5 : For Webserver Automation
 Press  6 : For LVM
 Press  7 : To exit the program
 """)
    
    ch=int(input("Enter Your Choice"))

    if ch == 1:
       docker() 

    elif ch == 2:
       hadoop()

    elif ch == 3:
       aws.aws()


    elif ch == 4:
       partition()


    elif ch == 5:
       webserver()            
        

    elif ch == 6:
       lvm()
       
    elif ch==7:
       exit()
        
    else:
        print("You Entered Wrong Choice ...")
