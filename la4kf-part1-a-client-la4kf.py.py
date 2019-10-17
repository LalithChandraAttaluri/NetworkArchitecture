import socket
host = socket.gethostbyname("10.205.7.26")
port = 2400
t = socket.socket()
t.connect((host,port))
msg = input("enter -->")
while True:
    if msg == 'Bye from Client Lalith Chandra Attaluri':
        t.send(msg.encode('utf-8'))
        data = t.recv(1024).decode('utf-8')
        print(data)
        break
        msg = input()
    elif msg == 'Hello from Client Lalith Chandra Attaluri':
        t.send(msg.encode('utf-8'))
        data = t.recv(1024).decode('utf-8')
        print(data)
        msg = input()
    else:
        t.send(msg).encode('utf-8')
        data = t.recv(1024).decode('utf-8')
        print(data)
t.close()
