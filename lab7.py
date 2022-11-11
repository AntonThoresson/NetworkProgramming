import socket
import select

port = 60003
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("", port))
sockL.listen(1)

listOfSockets = [sockL]

print("Listening on port {}".format(port))

while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]

    if sock == sockL:
        (sockClient, addr) = sockL.accept()
        listOfSockets.append(sockClient)
        sockClient.send(bytearray("{} Connected".format(sockClient.getpeername()), "ascii"))

        for socket in listOfSockets:
            if socket != sockL and socket != sockClient:
                socket.send(bytearray("{} connected".format(sockClient.getpeername()), "ascii"))
    else:
        data = sock.recv(2048)
        if not data:
            listOfSockets.remove(sock)
            peername = sockClient.getpeername()
            sock.close()

            for socket in listOfSockets:
                if (socket != sockL):
                    socket.send(bytearray("{} disconnected".format(peername), "ascii"))

        else:
            clientName = "{} ".format(sockClient.getpeername())
            for socket in listOfSockets:
                if socket != sockL:
                    clientMessage = clientName + data.decode("ascii")
                    socket.send(bytearray(clientMessage, "ascii"))






