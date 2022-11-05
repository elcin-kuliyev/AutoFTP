import update
import os
from re import match
OS = os.popen("lsb_release -ds").read()

result = match(r'Ubuntu', OS.strip())
if result.group(0) == "Ubuntu":
	update.update_ubuntu()