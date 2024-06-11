import socket
server = socket.socket()
hostIp = socket.gethostname()
port = 23956
print("Starting server...")
server.bind((hostIp, port))
print("Start lisenning...")
server.listen(1)

con, addr = server.accept()

print("Connection:   ", con)
print("Client address:    ", addr)

messenge = "Hello, client. This is test text."

con.send(messenge.encode())
con.close()
print("Close server")
server.close()
