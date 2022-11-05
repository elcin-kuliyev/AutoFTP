import os
from subprocess import check_call
from re import match
OS = os.popen("lsb_release -ds").read()


result = match(r'Ubuntu', OS.strip())



for result.group(0) in ["Ubuntu", "Debian", "Linux Mint", "Kali Linux", "Parrot OS"]:
	# install update and upgrade system
	check_call("sudo apt-get update ", shell=True)
	check_call("sudo apt-get upgrade -y ", shell=True)



