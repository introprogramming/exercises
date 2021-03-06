# http://learning-0mq-with-pyzmq.readthedocs.org/en/latest/pyzmq/patterns/pair.html

import time

import zmq

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:{}".format(port))

while True:
    msg = socket.recv()
    print(msg)
    socket.send_string("client message to server1")
    socket.send_string("client message to server2")
    time.sleep(1)
