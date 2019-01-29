from socket import *
sockfd = socket()

sockfd.connect(('176.221.15.210',8886))

sockfd.send('data'.encode())
sockfd.recv(1024)
print("end")
sockfd.close()