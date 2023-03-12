import threading
import socket
name = input('Enter ur name ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))


def client_receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == "what is ur name?":
                client.send(name.encode('utf-8'))
            else:
                print(msg)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        msg= f'{name}: {input("")}'
        client.send(msg.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
