import threading
import socket

host = '127.0.0.1' 
# HOST IP address is 'localhost' here
port = 9999
# PORT number ( can vary from 0 to 65536)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AddressFamily: AF_INET (IPv4) or AF_INET6 (IPv6)
#SocketKind: SOCK_STREAM(Transmission Control Protocol) or SOCK_DGRAM(User Datagram Protocol)

server.bind((host, port))
# 2 brackets otherwise error msg of 1 argument and 2 given

server.listen(10)
# backlog is the max no of unaccepted connxns allowed

print('Server is running')

clients = []
names = []



def send_msg(msg):
    # Function to send msg to all clients
    for client in clients:
        client.send(msg)

def handle_client(client):
    # Function to handle clients'connections
    while True:
        try:
            msg = client.recv(1024).decode()
            #max 1024 bits can be receives
            send_msg(msg.encode())
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            send_msg(f'{name} has left the chat room!'.encode('utf-8'))
            names.remove(name)
            break

def receive():
    # Function to receive the clients connection
    while True:
        client, addr = server.accept()
        #client is new socket object and addr is addr of socket whose connxn being accepted

        print(f'connection is established with {str(addr)}')
        client.send('what is ur name?'.encode('utf-8'))
        #utf-8 is encoding std: Unicode Tranformation Format-8 bit

        name = client.recv(1024).decode()
        names.append(name)
        clients.append(client)
        print(f'The name of this client is {name}')
        send_msg(f'{name} has joined the chat room'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()
