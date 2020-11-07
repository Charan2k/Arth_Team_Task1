import os

def webserver():
	print("""------------------MENU------------------
	1. Install the Web Server
	2. Configure the Web Server
	3. Start the Web Server
	4. Stop the Web Server
	5. Check Status of Web Server 
	""")

	choice = int(input("Enter your choice: "))
	if(choice==1):
		os.system("yum install httpd")
		print("Installed Successfully\n")


	elif(choice==2):
		os.system("systemctl enable httpd")
		print("Enabled HTTPD Services permanently\n")


	elif(choice==3):
		os.system("systemctl start httpd")
		print("Web Server Started Successfully\n")


	elif(choice==4):
		os.system("systemctl stop httpd")
		print("Web Server Stopped Successfully\n")


	elif(choice == 5):
		os.system("systemctl status httpd")


	else:
		print("Invalid Choice...")
