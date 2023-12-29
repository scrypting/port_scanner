import socket
import sys
from datetime import datetime

target = input("Please enter the name of the Host you would like to scan: ")
host = socket.gethostbyname(target)

try:
    file = open("Port-Scanner-1.txt", "w")
except FileExistsError:
    print("File Exists Error")
    sys.exit()

date = datetime.date(datetime.now())
t1 = datetime.now()

print("Start Time: {}".format(t1.strftime("%H:%M:%S")))
file.write("Start Time: {} \n\n".format(t1.strftime("%H:%M:%S")))

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.01)
        result = sock.connect_ex((host, port))
        if result == 0:
            try:
                print('Port No : {} Open Protocol Service Name: {}'.format(port, socket.getservbyport(port, "tcp")))
                file.write('Port No : {} Open Protocol Service Name: {}\n'.format(port, socket.getservbyport(port, "tcp")))
            except socket.error:
                print("Port No: {} Open Protocol Service Name: {}".format(port, "Unknown"))
                file.write("Port No: {} Open Protocol Service Name: {}\n".format(port, "Unknown"))
except socket.gaierror:
    print("Sorry, I could not connect to the Server. Exiting")
    file.write("\n\nSorry, I could not connect to the Server. Exiting")

file.close()
