import socket
host='10.151.7.90'
port=2400
t=socket.socket()
t.connect((host,port))
msg=input("Press enter to send file -->")
g=open('client.txt','rb')
n=g.read()
while True:
    if msg=='exit':
       t.send(msg.encode("utf-8"))
       data=t.recv(256000000).decode("utf-8")
       print(str(data))
       t.close()
    else:
       t.send(n)
       break
a = "done sending"
t.send(a.encode("utf-8"))
data = t.recv(256000000).decode("utf-8")
print(str(data))
msg=input()
