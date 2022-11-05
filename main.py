import os
OS = os.system("lsb_release -ds").read())
print(OS)
print(type(OS))
