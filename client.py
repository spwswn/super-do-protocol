from socket import*
import re
serverPort = 16700
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1', serverPort))
print(clientSocket.recv(1024).decode())
n = input("")
if re.match(r"^FIBO (\d+)",n):
    res = re.match(r"^FIBO (\d+)",n)
    clientSocket.send(res.group(1).encode())
    m = clientSocket.recv(1024).decode()
    print(m)
else:
    notKnow = "k"
    clientSocket.send(notKnow.encode())
    print(clientSocket.recv(1024).decode())
print(clientSocket.recv(1024).decode())
clientSocket.close()