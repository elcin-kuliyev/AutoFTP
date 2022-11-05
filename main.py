import os
OS = os.popen("lsb_release -ds").read()
#print(OS)
#print(type(OS))

if OS in "Ubuntu 22.04.1 LTS":
	print("Ubuntu")
else:
	print("Error")
