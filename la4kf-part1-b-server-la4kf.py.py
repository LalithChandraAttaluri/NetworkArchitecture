import socket
import os
host=socket.gethostbyname("10.151.2.20")
port=2400
t=socket.socket()
t.bind((host,port))
t.listen(1)
g,addr=t.accept()
while True:
    data = g.recv(256000000).decode('utf-8')
    if data == 'exit':
        d = 'Server Gone'
        g.send(d.encode("utf-8"))
        break
    else:
        h = open('client.txt','w')
        h.write(data)
        h.close()
        print(str(data))
        b=data +'\nAdded by the server'
        g.send(b.encode("utf-8"))
g.close()

