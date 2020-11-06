import os

def keypair():
	print("""------------------MENU------------------
	1. Create a key-pair
	2. Describe a key-pair
	3. Delete a key-pair
	""")
	choice = int(input("Enter your Choice: "))
	keyname = input("Enter the key name: ")
	if(choice==1):
		#create
		os.system("aws ec2 create-key-pair --key-name {}".format(keyname))


	elif(choice==2):
		#describe
		os.system("aws ec2 describe-key-pairs --key-name {}".format(keyname))


	elif(choice==3):
		#delete
		os.system("aws ec2 delete-key-pair --key-name {}".format(keyname))

"""
n = int(input("Enter your choice: "))
with open('ami-image-ids.txt','r') as f:
	i = 0
	while(i<n):
		id = f.readline()
		i = i + 1
#print(type(id))
os.system("aws ec2 run-instances --image-id {}".format(id))
"""

def securityGroup():
	print("""------------------MENU------------------
	1. Create a security-group
	2. Describe a security-group
	3. Delete a security-group
	""")
	choice = int(input("Enter your Choice: "))
	groupname = input("Enter the group name: ")
	if(choice==1):
		#create
		group_description = input("Described by name: ")
		os.system("aws ec2 create-security-group --group-name {} --description \"{}\" ".format(groupname,group_description))

	elif(choice==2):
		#describe
		os.system("aws ec2 describe-security-groups --group-name {}".format(groupname))

	elif(choice==3):
		#delete
		os.system("aws ec2 delete-security-group --group-name {}".format(groupname))

def instances():
	print("------------------MENU------------------")
	print("""
	 Press  1 : To Launch an instance
	 Press  2 : To Start an Instance
	 Press  3 : To Stop an Instance 
	 Press  4 : To Describe All Instances 
	 Press  5 : To Create a Volume
	 Press  6 : To Attach volume with instance
	""")

	ch = int(input("Enter your choice: "))

	if ch == 1:
		print("""------------------MENU------------------
		1. Amazon Linux
		2. Redhat Linux.
		3. Ubuntu:lastest
		4: Windows Server
		""")
		n = int(input("Enter your choice: "))
		with open('ami-image-ids.txt','r') as f:
			i = 0
			while(i<n):
				ami_id = f.readline()
				i = i + 1
		print(ami_id)
		keyname = input("Enter the key name: ")
		groupname = input("Enter the security group name: ")
		os.system("aws ec2 run-instances --instance-type t2.micro --key-name {} --security-groups {} --image-id {}".format(keyname,groupname,ami_id))


	elif ch == 2:
		instance_id = input("Enter Instance Id : ")
		os.system(" aws ec2 start-instances --instance-id {}".format(instance_id))


	elif ch == 3:    
		instance_id = input("Enter Instance Id : ")
		os.system(" aws ec2 stop-instances --instance-id {}".format(instance_id))


	elif ch == 4:
		os.system("aws ec2 describe-instances")

		
	elif ch == 5: 
		print("Enter Size : ",end = "")
		size = input()
		print("Enter Availability Zone : ",end = "")
		zone = input()
		print("Enter Volume Type : ",end= "")
		volume_type = input()
		os.system(" aws ec2 create-volume  --availability-zone {} --size {} --volume-type {}".format(zone,size,volume_type))


	elif ch == 6:
		print("\t\t\tVolume Zone & Instance Zone Must be same !!!")
		print("\t\t\t--------------------------------------------")
		os.system("tput setaf 7")
		print("Enter volume-id : ",end = "")
		volume_id = input()
		print("Enter instance-id : ",end = "")
		instance_id = input()
		print("Enter device : /dev/",end= "")
		device = input()
		os.system(" aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{} ".format(volume_id,instance_id,device))


def aws():
	print("""------------------MENU------------------
	1. Key-Pair Menu
	2. Security-Group Menu
	3. EC2 Instances
	4. Exit
	""")

	choice = int(input("Enter your choice: "))

	if choice == 1:
		keypair()


	elif choice == 2:
		securityGroup()


	elif choice == 3:
		instances()


	elif choice == 4:
		print("Exiting...")

		
	else:
		print("Invalid Choice")
