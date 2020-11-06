import os 

print("Press 1: To Start your Name Node")
print("Press 2: To check hadoop services are running")
print("Press 3: TO stop your name node")
print("Press 4: To start your data node")
print("Press 5: To check hdfs file system") 
print("Press 6 : To stop the datanode")
print("Press 7: To check the report")
i=int(input("Enter your choice"))
if i==1:
        os.system("hadoop-daemon.sh start namenode")
elif i==2:
	print("Press 1 for checking namenode service")
	print("Press 2 for checking datanode service")
	k=int(input("Enter the choice"))
	if k==1:
		os.system("jps")
	elif k==2:
		j=input("Enter the ip of data node")
		os.system("ssh {} jps".format(j))	
elif i==3:
	os.system("hadoop-daemon.sh stop namenode")
elif i==4:
	b=int(input("Enter the no of data nodes you want to start"))
	for i in range(b):
		j=input("Enter the Ip address of node {}".format(i))
		os.system("ssh {} hadoop-daemon.sh start datanode".format(j))
elif i==5:
	os.system("hadoop fs -ls /")		
elif i==6:
	i=input("Enter the Ip address of the data node to stop")
	os.system("ssh {} hadoop-daemon.sh stop datanode".format(i))
	
elif i==7:
	os.system("hadoop dfsadmin -report")
	
else:
	print("Wrong choice")
	 
