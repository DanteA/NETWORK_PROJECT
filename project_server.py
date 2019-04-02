import socket
import threading
import Queue  # renamed to queue in 3
import select
# import game

"""SERVER CODE"""
# TODO: stop-and-wait, pipelining, flow and congestion control
questions = {
        1: "Which protocol sends its data in reliable, in-order manner? "
           "\n A. UDP \n B. TCP \n C. HTTP \n D. IP",
        2: "What OSI Model layer is responsible for breaking the data down into segments? "
           "\n A. Transport Layer \n B. Network Layer \n C. Link Layer \n D. Physical Layer",
        3: "What do you call the electromagnetic interference of one wire to another? "
           "\n A. EMI \n B. RFI \n C. Crosstalk \n D. Static",
        4: "What field is used to indicate how long a packet has until it is discarded by the network? "
           "\n A. Protocol \n B. TTL \n C. DS \n D. System clock",
        5: "How many bits does an IPv6 IP Address contain? "
           "\n A. 64 \n B. 32 \n C. 256 \n D. 128"

    }

answers = {
        1: "B",
        2: "A",
        3: "C",
        4: "B",
        5: "D"
    }


# RETURNS BOOLEAN checks if the input char is equivalent to the expected answer.
def checkinput(input, number):
    answerconvert = answers.get(number, 'IndexOutOfBounds from checkinput()')
    if input == answerconvert:
        return True
    else:
        return False


# asks for the number of the question you want to ask. Returns the question in string format.
# def getquestion(number):
#     return questions.get(number, "IndexOutOfBounds from getquestion()")
#
#
# def getquestionset(number):
#     question = getquestion(number)
#     return {question, answers.get(number, "IndexOutOfBounds from getquestionset()")}


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
    recv_packets = Queue.Queue()  # connection's queue for data

    print('Server Running...')

    player_names = []
    scores = []
    max_players = 3

    threading.Thread(target=recv_data, args=(s, recv_packets)).start()
    # WAIT FOR PLAYERS
    while len(clients) < max_players:
        data, addr = recv_packets.get()
        if addr not in clients:
            clients.add(addr)
            player_names.append(str(data))  # list player names
            scores.append(0)
            print("Player List {}".format(player_names))

    # ANNOUNCE GAME START
    print("Game Start")
    for c in clients:
        s.sendto("Game Start", c)

    # GAME PROPER
    for q in questions:
        answers_submitted = []
        # SEND QUESTIONS
        for c in clients:
            s.sendto(str(questions[q]), c)  # send question to all clients
        # RECEIVE ANSWERS
        for c in clients:
            data, addr = recv_packets.get()
            answers_submitted.append(str(data)[-1])  # remove player name from submitted answer
        print("Submitted Answers: {}".format(answers_submitted))
        # AWARD POINTS
        for a in range(0, len(answers_submitted)):
            print a
            if checkinput(answers_submitted[a], q):
                scores[a] += 1
            print("Total Points: {}".format(scores))

    # ANNOUNCE WINNER
    for c in clients:
        s.sendto("Total Points: {}".format(scores), c)  # announce results to all clients
        for i in range(0, len(scores)):
            if scores[i] == max(scores):
                s.sendto("WINNER: " + str(player_names[i]) + " - " + str(max(scores)) + "pts", c)
        s.sendto("Game Over. Thanks for playing!", c)

    s.close()


if __name__ == '__main__':
    run_server()
