import os
OS = os.popen("lsb_release -ds").read()
#print(OS)
#print(type(OS))

if OS.strip() in "Ubuntu 22.04.1 LTS\\n":
	print("Ubuntu")
else:
	print("Error")
