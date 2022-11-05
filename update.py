import os
from subprocess import check_call
from re import match
OS = os.popen("lsb_release -ds").read()

result = match(r'Ubuntu', OS.strip())

def update_ubuntu():
    check_call("sudo apt-get update ", shell=True)  # update server
    check_call("sudo apt-get upgrade -y ", shell=True)  # upgrade server
    check_call("sudo apt-get install vsftpd", shell=True)  # install FTP server
    check_call("sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.original", shell=True)  # Backup server conf

