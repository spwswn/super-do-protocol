from socket import *
import re

def fibo(x):
    if x==1:
        return 1
    if x==0:
        return 0
    return fibo(x-1) + fibo(x-2)

serverPort = 16700
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('0.0.0.0', serverPort))
serverSocket.listen(1)
print('The Super Do Server is ready to recieve message.')
accept_message = "200 OK connected Super Do Server."
close_message = "200 OK closed Super Do Server."
error_message = "404 NOT FOUND do not know this command."
while True:
    connetionSocket, addr = serverSocket.accept()
    connetionSocket.send(accept_message.encode())
    n = connetionSocket.recv(1024).decode()
    if re.match(r"^\d+", n):
        m = str(fibo(int(n)))
        text = f"200 OK fibo({n}) is {m}"
        connetionSocket.send(text.encode())
    else:
        connetionSocket.send(error_message.encode())
    connetionSocket.send(close_message.encode())
    connetionSocket.close()
