
import os
import getpass
import docker
import hadoop
import webserver
import partition

# print("------------------Welcome to Automation of Different Technologies Menu------------------")

print("\t\t\t--------------------------------------")

passwd = getpass.getpass("Enter your password: ")

if passwd != "toor":
   print("password is incorrect....")
   exit()

while(True):
    print("""\n\n------------------MENU------------------
 Press  1 : Docker Functions
 Press  2 : Hadoop Functions
 Press  3 : AWS CLI
 Press  4 : Linux Partitions
 Press  5 : Web Server
 Press  6 : Exit
 """)
    
    ch=int(input("Please select one of the sub menus: "))

    if ch == 1:
        docker.docker() 

    elif ch == 2:
        hadoop.hadoop()

    elif ch == 3:
        print("Aws not available")


    elif ch == 4: 
        partition.partition()


    elif ch == 5:
        webserver.webserver()            
        

    elif ch == 6:
        exit()
        
    else:
        print("You Entered Wrong Choice ...")
