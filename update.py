from os import popen
from subprocess import check_call
from re import match
import pyufw

OS = popen("lsb_release -ds").read()

result = match(r'Ubuntu', OS.strip())

def update_ubuntu():
    check_call("sudo apt-get update ", shell=True)  # update server
    check_call("sudo apt-get upgrade -y ", shell=True)  # upgrade server

def ubuntu_vsftpd():
    check_call("sudo apt-get install vsftpd -y", shell=True)  # install FTP server
    check_call("sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.original", shell=True)  # Backup server conf

def ubuntu_firewall():
    ufw.enable()
    ufw.add("allow OpenSSH")
    ufw.add("allow 20/tcp")
    ufw.add("allow 21/tcp")
    ufw.add("allow 990/tcp")
    ufw.add("allow 40000:50000/tcp")
    check_call("sudo ufw status", shell=True)