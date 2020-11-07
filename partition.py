# Module for Automating Linux Partitions
import os

def partition():
    while(True):
        print("""\n\n------------------MENU------------------
        Press 1: To see the disk partition of your system
        Press 2: To perform partition
        Press 3: To format the partition
        Press 4: To mount the partition
        Press 5: To exit back to main menu
        """)

        ch=int(input("Enter your choice: "))
        if ch==1:
            os.system("fdisk -l")

        elif ch==2:
            i=input("Enter the name of disk")
            os.system("fdisk {}".format(i))

        elif ch==3:
            i=input("Enter the name of disk")
            os.system("mkfs.ext4 {}".format(i))

        elif ch==4:
            i=input("Enter the name of disk")
            j=input("Enter the name of directory which you want to mount")
            os.system("mount  {} {}".format(i,j))

        elif ch==5:
            break

        else:
            print("Invalid Choice")
        
