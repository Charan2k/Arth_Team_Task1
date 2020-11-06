# program for our menu driven project

from webserverAutomate import webserver
from automateHadoop import hadoop
from awsAutomate import aws
from docker import docker

if __name__ == "__main__":
    print("""------------------MENU------------------
    1. Hadoop Functions 
    2. AWS CLI
    3. Docker Functions
    4. Web Server
    """)

    choice = int(input("Please select one of the sub menus: "))
    if choice == 1:
        hadoop()
    
    elif choice == 2:
        aws()
    
    elif choice == 3:
        docker()

    elif choice == 4:
        webserver()

    elif choice == 5:
        print("Exiting...")

    else:
        print("Invalid Choice ")

