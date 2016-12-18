import socket
import logging
from threading import Thread
from user import User


class Client(User):
    # to create client we need to know username, some function which would 
    # display messages (it could be either graphical or console application)
    # and server's host and port
    def __init__(self, name, display, host='localhost', port=5000):
        logging.info("init client")

        super().__init__(name)

        self.display = display

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        self.sock.connect((host, port))

        logging.info("client connected")

        # starting to listen incoming messages
        Thread(target=self.receive_message).start()

    def receive_message(self):
        while True:
            logging.info("client received message")
            self.display(str(self.sock.recv(1024), 'utf8'))

    def send_message(self, msg):
        self.sock.send(bytes(msg, 'utf8'))
        logging.info("client send message")
