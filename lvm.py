import os

print("\t\t\tWelcome to partition menu")
print("\t\t\t-------------------------")

 
ch = int(input('''
    press 1: To check the information about the Harddisk    
    press 2: To create a Physical volume (PV) 
    press 3: To create Physical Volume (PV) + Volume Group (VG)
    press 4: To create Physical Volume(PV)+Volume Group(VG)+Logical Volume(LV)
    press 5: To mount it to a folder
    press 6: To exit
    Select : '''))

if ch == 1:
    os.system("fdisk -l")
  
if ch == 2:
    Disk1 =input("\n\nForm above input the name of disk you want to use : ")
    Disk2 =input("\nInput the second disk if not press enter: ")
    os.system("pvcreate {} {}".format(Disk1,Disk2))

elif ch == 33:
    name1 = input("Input the name of your Volume Group(VG): ")
    os.system("fdisk -l")
    Disk1 =input("\n\nWhich disk you want to use : ")
    Disk2 =input("\nSelect the second disk if not press enter: ")
    os.system("pvcreate {} {}".format(Disk1,Disk2))
    os.system("vgcreate {} {} {}".format(name1,Disk1,Disk2))

elif ch == 4:    
    name1 = input("Input the name of your Volume Group(VG): ")
    name2 = input("Input the name of your Logical Volume(LV): ")
    size1 = input("Input the Size in GB : ")
    os.system("fdisk -l")
    Disk1 = input("\n\nWhich disk you want to use : ")
    Disk2 =input("\nSelect the second disk if not press enter: ")
    os.system("pvcreate {} {}".format(Disk1,Disk2))
    os.system("vgcreate {} {} {}".format(name1,Disk1,Disk2))
    os.system("lvcreate --size {}G --name {} {}".format(size1,name2,name1))
    os.system("lvdisplay {}/{}".format(name1,name2))

elif ch == 5:
    volume=input("Enter the name of volume Group: ")
    name=input("Enter the name of LVM: ")
    mount_point=input("Input the LVM mountpoint name: ")
    os.system("mount /dev/{} /{} /{}".format(volume,name,mount_point))

elif ch == 6:
    print("Exiting....")

else:
   print("Select the correct option")

