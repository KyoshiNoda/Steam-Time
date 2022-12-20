import socket
import threading
import sys

from _thread import *


lock = threading.Lock()

def server_listener(c):
    while True:
        data = c.recv(1024)
        if not data:
            print('Bye')
            lock.release()
            break
        c.send(data)
    c.close()

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
        c, addr = s.accept()
        lock.acquire()
        print("Connected to :{} :{}", addr[0], addr[1])

        start_new_thread(server_listener, (c))
    s.close()

if __name__ == '__main__':
    main()