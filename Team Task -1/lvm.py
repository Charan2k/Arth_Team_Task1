# Module for LVM Automation
import os

def lvm():

    while(True):
                       
        print("\t\t\tWelcome to LVM menu")
        
        print("\t\t\t-------------------------")
         
        print('''
press 1: To check the information about the Harddisk    
press 2: To create a Physical volume (PV)
Press 3: To display info of Physical Volume (PV)
Press 4: To create a Volume Group (VG) 
press 5: To display info of Volume Group
Press 6: To create the LVM
press 7: To mount it to a folder
press 8: To exit
            ''')
        ch=int(input("Enter your choice: "))
        
        if ch == 1:
            os.system("fdisk -l")
            
        elif ch==2:
            i=int(input("Enter number of Physical Volumes you want to create"))
            for j in range(i):
                disk=input("Enter the name of disk {}".format(j))
                os.system("pvcreate /dev/{}".format(disk))

        elif ch==3:
            disk=input("Enter the name of Physical Volume to display")
            os.system("pvdisplay /dev/{}".format(disk))
            
        elif ch == 4:
            name1 = input("Input the name of your Volume Group(VG): ")
            os.system("fdisk -l")
            
            i=int(input("Enter the no of Physical Volumes you want to group"))
            
            for j in range(i):
                  disk=input("Enter the name of Physical Volume {} : ".format(j+1))
                  os.system("vgcreate {} /dev/{}".format(name1,disk))
        elif ch == 5:
                  i=input("Enter the name of volume group: ")
                  os.system("vgdisplay {}".format(i))
        elif ch==6:
                  name1 = input("Input the name of your Volume Group(VG): ")
                  name2 = input("Input the name of your Logical Volume(LV): ")
                  size1 = input("Input the Size in GB : ")
                  os.system("fdisk -l")
                  os.system("lvcreate --size {}G --name {} {}".format(size1,name2,name1))
                  os.system("lvdisplay {}/{}".format(name1,name2))
                  os.system("mkfs.ext4 /dev/{}/{}".format(name1,name2))

        elif ch == 7:
                  volume=input("Enter the name of volume Group: ")
                  name=input("Enter the name of LVM: ")
                  mount_point=input("Input the LVM mountpoint name: ")
                  os.system("mount /dev/{}/{} /{}".format(volume,name,mount_point))

        elif ch == 8:
                  print("Exiting....")
                  break
        else:
           print("Select the correct option")
