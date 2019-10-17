import socket
host=socket.gethostbyname("10.205.3.192")
port=2400
t=socket.socket()
t.bind((host,port))
t.listen(1)
g,addr=t.accept()
while True:
    data = g.recv(1024).decode('utf-8')
    print(data)
    if data == 'Bye from Client Yasaswini Marella':
        b='Bye from Server- Lalith Chandra Attaluri'
        g.send(b.encode("utf8"))
        break
    elif data == 'Hello from Client Yasaswini Marella':
        a = 'Hello from Server- Lalith Chandra Attaluri'
        g.send(a.encode("utf8"))
    else:
        print(data)
        g.send(data.encode("utf8"))
g.close()