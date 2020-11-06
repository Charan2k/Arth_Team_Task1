import os
import getpass


def docker():
    print("""------------------DOCKER MENU------------------
        Press  1 : To Check the available Docker Images
        Press  2 : To Pull a Docker Image from the DockerHub
        Press  3 : To To launch docker Container
        Press  4 : To check the running Containers
        Press  5 : To check all the Containers
        Press  6 : To delete the Container
        Press  7 : To delete a Docker Image
        Press  8 : To search for an image
        Press  9 : To Exit
        """)

    ch=int(input("Enter your choice: "))

    if ch == 1:
        os.system("docker images")


    elif ch == 2:
            img_name = input("Enter image name: ")
            os.system("docker pull {}".format(img_name))


    elif ch == 3:
        cont_name = input("Enter Container name: ")
        img_name = input("Enter docker image name: ")
        os.system(" docker run -dit --name {} {}".format(name1,name2))


    elif ch == 4:
        print(" Running Containers")
        os.system(" docker ps ")


    elif ch == 5:    
        print("All the Containers in your Docker Container Engine: ")
        os.system(" docker ps -a")


    elif ch == 6:
        cont_name = input("Enter the name of container: ")
        os.system(" docker rm -f {} ".format(cont_name))


    elif ch == 7:
        img_name = input("Enter the name of image: ")
        os.system("docker rmi {}".format(img_name))


    elif ch == 8:
        img_name = input("Enter the image name: ")
        os.system("docker search {}".format(img_name))


    elif ch == 9:
        print("Exiting....")


    else:
        print("You Entered Wrong Choice ...")
