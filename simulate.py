import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
s.bind(('localhost', 9000))

while True:
    s.listen(0)
    (clientsocket, address) = s.accept()