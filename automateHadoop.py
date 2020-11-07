import os 

def hadoop():
	print("""------------------MENU------------------
	Press 1 : To Start your Name Node
	Press 2 : To check hadoop services are running
	Press 3 : TO stop your name node
	Press 4 : To start your data node
	Press 5 : To check hdfs file system 
	Press 6 : To stop the datanode
	Press 7 : To check the report
	""")

	choice=int(input("Enter your choice"))
	if choice == 1:
		os.system("hadoop-daemon.sh start namenode")

	elif choice == 2:
		print("Press 1 for checking namenode service")
		print("Press 2 for checking datanode service")
		k=int(input("Enter the choice"))
		if k == 1:
			os.system("jps")
		elif k == 2:
			j = input("Enter the ip of data node")
			os.system("ssh {} jps".format(j))

	elif choice == 3:
		os.system("hadoop-daemon.sh stop namenode")

	elif choice == 4:
		b = int(input("Enter the no of data nodes you want to start"))
		for i in range(b):
			j = input("Enter the Ip address of node {}".format(i))
			os.system("ssh {} hadoop-daemon.sh start datanode".format(j))

	elif choice == 5:
		os.system("hadoop fs -ls /")

	elif choice == 6:
		choice = input("Enter the Ip address of the data node to stop")
		os.system("ssh {} hadoop-daemon.sh stop datanode".format(i))

	elif choice == 7:
		os.system("hadoop dfsadmin -report")

	else:
		print("Wrong choice")