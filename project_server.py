import socket
import threading
import queue  # renamed to queue in 3.7
import game
"""SERVER CODE"""
# TODO: stop-and-wait, pipelining, flow and congestion control
# TODO: quiz game code


def recv_data(sock, recv_packets):
    while True:
        data, addr = sock.recvfrom(1024)
        recv_packets.put((data, addr))


def run_server():
    host = socket.gethostbyname(socket.gethostname())
    port = 5000
    print('Server hosting on IP->' + str(host))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    clients = set()
    recv_packets = queue.Queue()

    print('Server Running...')

    threading.Thread(target=recv_data, args=(s, recv_packets)).start()
    while True:
        while not recv_packets.empty():
            data, addr = recv_packets.get()
            if addr not in clients:
                clients.add(addr)
                continue
            # clients.add(addr)
            data = data.encode('utf-8')
            if data.endswith('qqq'):
                clients.remove(addr)
                continue
            print(str(addr) + data)
            for c in clients:
                if c != addr:
                    s.sendto(data.encode('utf-8'), c)
    s.close()


if __name__ == '__main__':
    run_server()
