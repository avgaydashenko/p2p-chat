import socket
import logging
from threading import Thread
from user import User


class Server(User):
    # to create server we need to know username, some function which would 
    # display messages (it could be either graphical or console application)
    # and server's host and port
    def __init__(self, name, display, host='localhost', port=5000):
        logging.info("init server")

        # creating user with given name
        super().__init__(name)

        self.display = display

        # creating TCP/IP connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        sock.bind((host, port))
        sock.listen()
        self.conn, self.addr = sock.accept()

        logging.info("server started")

        # starting to listen incoming messages
        Thread(target=self.receive_message).start()

    def receive_message(self):
        while True:
            if self.addr:
                logging.info("server received message")
                self.display(str(self.conn.recv(1024), 'utf8'))

    def send_message(self, msg):
        self.conn.send(bytes(msg, 'utf8'))
        logging.info("server send message")
