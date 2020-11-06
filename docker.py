import os
import getpass

print("\t\t\tWelcome to Docker Menu")

print("\t\t\t--------------------------------------")



print("\t\t\t\t\tMenu")
print("\t\t\t\t\t----")
print("""
 Press  1 : To Check the available docker images
 Press  2 : To Pull docker image
 Press  3 : To To launch docker container
 Press  4 : To check the running containers
 Press  5 : To delete the container
 Press  6 : To Exit
""")

print("Enter Your Choice : ",end="")

ch=int(input())


if ch == 1:

    os.system("docker images")

elif ch == 2:
        img = input("Enter image name: ")
        os.system("docker pull {}".format(img))

elif ch == 3:

    name1 = input("Enter COntainer name: ")
    name2 = input("Enter docker image name: ")
    os.system(" docker run -dit --name {} {}".format(name1,name2))


elif ch == 4:
    
    print(" Running Containers")
    os.system(" docker ps ")


elif ch == 5:

   
    name1 = input("Enter the name of container: ")
    os.system(" docker rm -f {} ".format(name1))

elif ch == 6:
    exit()
    
else:
    print("You Entered Wrong Choice ...")


