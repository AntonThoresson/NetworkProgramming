import socket



def server():
    sockS = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sockS.bind(("0.0.0.0", 8000))
    sockS.listen(1)

    while True:
        (sockC, addr) = sockS.accept()
        data = sockC.recv(1024).decode("ascii")
        if not data:
            break
        print(data)
        sockC.sendall(bytearray("HTTP/1.1 200 OK \n", "ascii"))
        sockC.sendall(bytearray("\n", "ascii"))
        sockC.sendall(bytearray("<html><body><h1>Your browser sent the following request</h1></body>\n", "ascii"))
        sockC.sendall(bytearray("<pre>" + data + "</pre>", "ascii"))
        sockC.sendall(bytearray("</html>", "ascii"))
        sockC.close()



server()

