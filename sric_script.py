# to do:
# make secure

# import everything yo
import time, socket, ftplib, os, argparse
from ftplib import FTP

# handles arguments through command line
parser = argparse.ArgumentParser()
parser.add_argument("userIP", type=str, help="Target IP")
parser.add_argument("userName", type=str, help="Target User")
parser.add_argument("userPWD", type=str, help="Target Password")
parser.add_argument("dir", type=str, help="Target Directory")
parser.add_argument("upload", type=str, help="File for upload")
parser.add_argument("download", type=str, help="File for download")
args = parser.parse_args()

# function to upload file to specified ftp server
def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)

# function to download file from specified ftp server
def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print "Error"

# ftp server IP and credentials, set through command line arguments
port=21
ip = args.userIP
user = args.userName
password = args.userPWD
directory = args.dir
uploadFile = args.upload
downloadFile = args.download

# loops until the end of time (or something)
while (True):
    # attemps connection
    try:
        # makes connection to IP and starts ftp session with credentials
        s=socket.socket()
        s.connect((ip,port))
        ftp=FTP(ip)
        ftp.login(user,password)
        ftp.cwd(directory)
        # prints file list only for testing
        print "File List:"
        files = ftp.dir()

        print "Uploading file..."
        upload(ftp, uploadFile)
        print "Downloading file..."
        getFile(ftp, downloadFile)

        # Prints files in directory for testing again
        print "New File List:"
        files = ftp.dir()

        # exits program after file has been uploaded and other downloaded hopefully
        break
    except IOError as e:
        print "Looking for connection..."
