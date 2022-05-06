# coding=utf-8
import socket
import threading


class Server:
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        while True:
            try:
                # self.port = int(input('Enter port number to run on --> '))
                self.port = 6666
                self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.tcp_socket.bind((self.ip, self.port))

                break
            except:
                print("Couldn't bind to that port")

        self.connections = []
        self.accept_connections()

    def accept_connections(self):
        self.tcp_socket.listen(10)

        print('Running on IP: ' + self.ip)
        print('Running on port: ' + str(self.port))

        while True:
            conn, addr = self.tcp_socket.accept()

            self.connections.append(conn)

            threading.Thread(target=self.handle_client, args=(conn, addr,)).start()

    def broadcast(self, sock, data):
        for client in self.connections:
            if client != self.tcp_socket and client != sock:
                try:
                    client.send(data)
                except:
                    pass

    def handle_client(self, conn, addr):
        while True:
            try:
                data = conn.recv(1024)
                self.broadcast(conn, data)

            except socket.error:
                conn.close()


server = Server()
