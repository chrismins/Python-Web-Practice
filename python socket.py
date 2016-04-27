# Learn from Vamei
# Server side
import socket

# Address
HOST = ''
PORT = 8000   #此处的8000是作者自定义的端口，
# 还是有必须要用8000这个端口，
# 是否可以换成其它的端口

reply = 'yes'   #此处是什么意思？？

# Configure socket
s     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
                                      #此处的空行在什么情况下要空行
# passively wait, 3:maximum number of connections in the queue
s.listen(3)
# accept and establish connection
conn, addr = s.accept()
# receive message
request    = conn.recv(1024)

print 'request is:', request
print 'Connected by', addr
# send message
conn.sendall(reply)
# close connection
conn.close()







