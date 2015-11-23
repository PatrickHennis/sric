import time, socket, ftplib, os
from ftplib import FTP
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("userIP", type=str, help="Target IP")
parser.add_argument("userName", type=str, help="Target User")
parser.add_argument("userPWD", type=str, help="Target Password")
args = parser.parse_args()

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
ip = args.userIP
user = args.userName
password = args.userPWD

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
        print "Uploading file..."
        upload(ftp, "test2.txt")
        print "Downloading file..."
        getFile(ftp,'test.txt')

        print "New File List:"
        files = ftp.dir()
        break
    except IOError as e:
        #print "I/O error({0}): {1}".format(e.errno, e.strerror)
        print "Retrying..."
