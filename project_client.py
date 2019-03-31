import socket
import threading
import random
import os

"""CLIENT CODE"""


def receive_data(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(data.decode('utf-8'))
        except:
            pass

def run_client(server_ip):
    host = socket.gethostbyname(socket.gethostname())
    port = random.randint(6000, 10000)
    print('Client IP->' + str(host) + ' Port->' + str(port))
    server = (str(server_ip), 5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    name = input('Enter username: ')
    if name == '':
        name = 'Guest' + str(random.randint(1000, 9999))
    print('Your name is: ' + '[' + name + ']')
    s.sendto(name.encode('utf-8'), server)
    threading.Thread(target=receive_data, args=(s,)).start()
    while True:
        data = input()
        if data == 'qqq':
            break
        elif data == '':
            continue
        data = '[' + name + ']' + '->' + data
        s.sendto(data.encode('utf-8'), server)
    s.close()
    os._exit(1)


if __name__ == '__main__':
    run_client("192.168.100.3")


# 10.100.201.46