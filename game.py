#checks if the input char is equivalent to the expected answer.
def checkinput(input, number):
    answerconvert = answer.get(number, 'IndexOutOfBounds from checkinput()')
    if(input == answerconvert):
        return true
    else:
        return false

# asks for the number of the question you want to ask. Returns the question in string format.
def getquestion(number):
    questions = {
        1: "Which protocol sends its data in reliable, in-order manner? \n A. UDP \n B. TCP \n C. HTTP \n D. IP",
        2: "What OSI Model layer is responsible for breaking the data down into segments? \n A. Transport Layer \n B. Network Layer \n C. Link Layer \n D. Physical Layer",
        3: "What do you call the electromagnetic interference of one wire to another? \n A. EMI \n B. RFI \n C. Crosstalk \n D. Static",
        4: "What field is used to indicate how long a packet has until it is discarded by the network? \n A. Protocol \n B. TTL \n C. DS \n D. System clock",
        5: "How many bits does an IPv6 IP Address contain? \n A. 64 \n B. 32 \n C. 256 \n D. 128"

    }
    return questions.get(number, "IndexOutOfBounds from getquestion()")

def getquestionset(number):
    question = getquestion(number)
    answer = {
        1: "B",
        2: "A",
        3: "C",
        4: "B",
        5: "D"
    }

    return {question, answer.get(number, "IndexOutOfBounds from getquestionset()")}
