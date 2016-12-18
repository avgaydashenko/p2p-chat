from server import Server
from client import Client
from interface import Interface
import logging

logging.basicConfig(level=logging.DEBUG, format="%(filename)s, line:%(lineno)d # [%(asctime)s] %(message)s")
logging.info("start session")

# create graphical interface
# pass classes which handle server and client
Interface(handle_server=Server, handle_client=Client)