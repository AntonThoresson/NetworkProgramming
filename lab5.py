import socket 

port = 60003

def ruleEngine(serverAnswer, clientAnswer):
    serverWon = False
    clientWon = False

    if serverAnswer == clientAnswer:
        return serverWon, clientWon
    elif serverAnswer == "P":
        if clientAnswer == "R":
            serverWon = True
            return serverWon, clientWon
        else:
            clientWon = True
            return serverWon, clientWon
    elif serverAnswer == "S":
        if clientAnswer == "P":
            serverWon = True
            return serverWon, clientWon
        else:
            clientWon = True
            return serverWon, clientWon
    elif serverAnswer == "R":
        if clientAnswer == "S":
            serverWon = True
            return serverWon, clientWon
        else:
            clientWon = True
            return serverWon, clientWon

    return "Invalid input"
    


def serversideGetPlaySocket():
    sockS = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sockS.bind(("127.0.0.1", port))
    sockS.listen(1)

    winScore = 3 
    serverScore = 0
    clientScore = 0

    while True:
        print("\nlistening...\n")
        (sockC, addr) = sockS.accept()
        print("Connection from {}".format(addr))
        while True:
            data = sockC.recv(1024)
            if not data:
                break

            serverAnswer = input("Enter a move [R/P/S]: ")
            clientAnswer = data.decode("ascii")

            print("({},{}) Your move: {}".format(serverScore, clientScore, serverAnswer))
            print("Oppenent's move: {}".format(clientAnswer))
            sockC.sendall(bytearray("Oppenent's move: {}".format(serverAnswer), "ascii"))
            
            isServerWin, isClientWin = ruleEngine(serverAnswer, clientAnswer)

            if isServerWin:
                serverScore += 1
                sockC.sendall(bytearray("({},{}) ".format(serverScore, clientScore), "ascii"))
            elif isClientWin:
                clientScore += 1
                sockC.sendall(bytearray("({},{}) ".format(serverScore, clientScore), "ascii"))
            else:
                tieMessage = "Its a tie"
                print(tieMessage)
                sockC.sendall(bytearray(tieMessage, "ascii"))

            if serverScore | clientScore is winScore:
                sockC.close() 
                print("Disconnect from {}".format(addr))


def clientsideGetPlaySocket(host):
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect((host, port))
    global serverScore
    global clientScore
    
    while True:
        clientAnswer = input("Enter a move [R/S/P]: ")
        sock.sendall(bytearray(clientAnswer, "ascii"))

        data = sock.recv(1024)
        resultData = sock.recv(1024)
        result = resultData.decode("ascii")
        if result == "Its a tie":
            print(result)
        else:
            print("{}Your move: {}".format(result, clientAnswer))
        print(data.decode("ascii"))
    sock.close()






answer = "?"
while answer not in {"C", "S"}:
    answer = input("Do you want to be server (S) or client (C): ")
    if answer == "S":
        sock = serversideGetPlaySocket()
    else:
        host = input("Enter the server's IP: ")
        sock = clientsideGetPlaySocket(host)
