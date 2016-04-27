import socket
HOST ='183.206.176.41'
PORT =8000
request = 'can you hear me?'
# configure socket
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# send message
s.sendall(request)
# receive message
reply = s.recv(1024)
print 'reply is:',reply
# close connection
s.close()

