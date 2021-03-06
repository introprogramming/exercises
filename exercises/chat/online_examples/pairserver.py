# http://learning-0mq-with-pyzmq.readthedocs.org/en/latest/pyzmq/patterns/pair.html

import time

import zmq

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:{}".format(port))

while True:
    socket.send_string("Server message to client3")
    msg = socket.recv()
    print(msg)
    time.sleep(1)
