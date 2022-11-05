import os
import subprocess
OS = os.popen("lsb_release -ds").read()
#print(OS)
#print(type(OS))

if OS.strip() in "Ubuntu 22.04.1 LTS\\n":
	print("Ubuntu")
	subprocess.check_call("sudo apt-get update ", shell=True)

else:
	print("Error")