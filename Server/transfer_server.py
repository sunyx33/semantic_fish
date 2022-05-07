# coding=utf-8
import socket
import threading
import select


class TCPServer:
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        while True:
            try:
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
                data = conn.recv(4096)
                self.broadcast(conn, data)

            except socket.error:
                conn.close()


class UDPServer:
    def __init__(self, broadcast_port_list=None):
        self.host_ip = socket.gethostbyname(socket.gethostname())
        self.host_virtual_ip = "10.147.18.15"  # zerotier
        self.host_port = 8888
        if broadcast_port_list is None:
            self.broadcast_port_list = [6666]
        else:
            self.broadcast_port_list = broadcast_port_list

        # 创建广播接收器
        self.recvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.recvSocket.bind((self.host_ip, self.host_port))

        # 创建广播发送器
        self.sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sendSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sendSocket.bind((self.host_virtual_ip, self.host_port))

        self.inputs = [self.recvSocket]

        self.handle_client()

    def handle_client(self):
        print("server start")
        while True:
            try:
                # readable, writable, exceptional = select.select(inputs, [], [], 1.0)
                readable = select.select(self.inputs, [], [], 1.0)[0]
                for sock in readable:
                    data, _ = sock.recvfrom(4096)
                    if data:
                        for client_port in self.broadcast_port_list:
                            self.sendSocket.sendto(data, ('<broadcast>', client_port))
            except socket.error:
                print("broadcast error")


server = UDPServer()
