import socket
import threading
import sys
import steam

from _thread import *


lock = threading.Lock()

def server_listener(client):
    while True:
        data = client.recv(1024)
        if not data:
            print('Bye')
            lock.release()
            break
        client.send(data)
    client.close()

def main():
    host = ""
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, port))
    except socket.error as message:
        print('Bind failed. Error Code: {} Message {}',str(message[0]), str(message[1]))
        sys.exit()
    print("socket binded to {}", port)

    s.listen(5)
    print("socket is listening")

    while True:
        client, addr = s.accept()
        lock.acquire()
        print("Connected to :{} :{}", addr[0], addr[1])

        start_new_thread(server_listener, (client))
    s.close()

if __name__ == '__main__':
    main()