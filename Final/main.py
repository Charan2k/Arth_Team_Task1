
import os
import getpass
import docker
import hadoop
import webserver
import partition

print("\t\t\tWelcome to Automation of Different Technologies Menu")

print("\t\t\t--------------------------------------")

passwd = getpass.getpass("Enter your password: ")

if passwd != "toor":
   print("password is incorrect....")
   exit()

print("\t\t\t\t\tMenu")
print("\t\t\t\t\t----")



while(True):
    print("""
 Press  1 : For Docker
 Press  2 : For Hadoop
 Press  3 : For aws 
 Press  4 : For Partition 
 Press  5 : For Webserver Automation
 
""")
    
    ch=int(input("Enter Your Choice"))

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
