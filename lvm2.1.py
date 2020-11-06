import os
disk1=input("Enter first disk name: ")
volume=input("Enter the name of volume Group: ")
name=input("Enter the name of LVM: ")
size=input("Enter the size of LVM: ")
mount_point=input("Input the LVM mountpoint name: ")
#Creating PV
os.system("pvcreate /dev/"+disk1)
#Creating Volume Group
os.system("vgcreate "+volume+" /dev/"+disk1)
os.system("vgdisplay "+volume)
#Creating lvm using lvcreate
os.system("lvcreate --size +"+size+"G --name "+name+" "+volume)
#formatting the lvm to use the lvm
os.system("mkfs.ext4 /dev/"+volume+"/"+name)
#mounting
os.system("mkdir /"+mount_point)
os.system("mount /dev/"+volume+"/"+name+" "+"/"+mount_point)
os.system("cd /"+mount_point)
