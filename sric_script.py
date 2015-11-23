import time
import socket
import ftplib
import os
from ftplib import FTP

def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)

def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print "Error"

port=21
ip=""
password=""
user=""

while (True):
    try:
        s=socket.socket()
        s.connect((ip,port))
        ftp=FTP(ip)
        ftp.login(user,password)
        ftp.cwd('/files')
        #print ftp.pwd()

        print "File List:"
        files = ftp.dir()

        upload(ftp, "test2.txt")
        getFile(ftp,'test.txt')

        print "New File List:"
        files = ftp.dir()
        break
    except IOError as e:
        #print "I/O error({0}): {1}".format(e.errno, e.strerror)
        print "Retrying..."
