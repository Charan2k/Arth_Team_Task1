import os

def webserver():
	print("""--------MENU--------
	1. Install the Web Server
	2. Configure the Web Server
	3. Start the Web Server
	4. Stop the Web Server 
	""")

	choice = int(input("Enter your choice: "))
	if(choice==1):
		os.system("yum install httpd")
		print("\n Installed Successfully")

	elif(choice==2):
		os.system("systemctl enable httpd")
		print("\n Enabled web server permanently")

	elif(choice==3):
		os.system("systemctl start httpd")
		print("\n Web Server started Successfully")

	elif(choice==4):
		os.system("systemctl stop httpd")
		print("\n Web Server Stopped Successfully")

	else:
		print("Invalid Choice...")
