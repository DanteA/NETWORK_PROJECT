import socket
import threading
import random
import os

"""CLIENT CODE"""


def receive_data(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(str(data))
        except:
            pass


def run_client(server_ip):
    host = socket.gethostbyname(socket.gethostname())
    port = random.randint(6000, 10000)
    print('Client IP->' + str(host) + ' Port->' + str(port))
    server = (str(server_ip), 5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    # GET PLAYER NAME
    name = raw_input('Enter username: ')
    if name == '':
        name = 'Guest' + str(random.randint(1000, 9999))
    print('Your name is: ' + '[' + name + ']')
    s.sendto(str(name), server)
    # GET PLAYER ANSWER
    threading.Thread(target=receive_data, args=(s,)).start()
    while True:
        data = raw_input()
        if data != '':  # do not allow blank answers
            data = '[' + name + ']' + '->' + data
            s.sendto(str(data), server)

    s.close()
    os._exit(1)


if __name__ == '__main__':
    run_client("192.168.1.2")
