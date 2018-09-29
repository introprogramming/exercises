import socket
import sys
import time
from multiprocessing import Process, Lock

import zmq


# print zmq.pyzmq_version()


def receive_loop(connect_to, channel):
    """Connects to a client on this channel. Listens for and prints messages indefinitely."""
    local_context = zmq.Context()
    subscribe = local_context.socket(zmq.SUB)
    subscribe.setsockopt(zmq.SUBSCRIBE, channel)

    try:
        subscribe.connect(connect_to)
    except zmq.error.ZMQError:
        print("## Trouble connecting... :P Check if the adress is correct.")
        return

    while True:
        # print "Awating message..."
        print(subscribe.recv())
        time.sleep(0.005)


def start_listener(connect_to):
    """Creates a new daemon listener thread to this client on this channel (ie topic). Stores thread in `connections`."""
    global filter
    p = Process(target=receive_loop, args=(connect_to, filter))
    p.daemon = True

    c_lock.acquire()
    connections.append({'process': p, 'channel': filter, 'client': connect_to})
    c_lock.release()

    p.start()


def connect():
    """Parses input for an ip and a port. Uses the input to start a connection."""
    print("Connect to...")
    address = input("address (ip): ")
    if address == "":
        address = "localhost"
    try:
        port = int(input("port: "))
        connect_to = "tcp://%s:%s" % (address, port)
    except:
        print("## Error! Should look like '192.168.0.1 5556'")
        return

    start_listener(connect_to)


def help():
    """Prints available commands and what they do."""
    print("""
           Commands:
           \\exit\tExits the program
           \\help\tPrints this help
           \\connect\tConnect to another chat client
           \\disconnect <ch_name>\tDisconnects from all clients using this channel
           \\channel <ch_name>\tWrites to this chat channel only""")


def disconnect(channel):
    """Stops all processes that listens on a certain channel."""
    c_lock.acquire()
    # print("## Disconnecting from '"+channel+"'...")
    for entry in connections:
        if entry['channel'] == channel:
            connections.remove(entry)
            entry['process'].terminate()
    c_lock.release()


def io_loop():
    """Loop for main (IO) thread. Handles user input such as commands and chat messages to send."""
    help()
    while True:
        global filter
        inp = input()
        if inp.startswith('\\'):
            # command
            if inp.startswith('\\exit'):
                break
            elif inp.startswith('\\connect'):
                connect()
            elif inp.startswith('\\disconnect'):
                try:
                    channel = inp.split(' ')[1]
                except:
                    print("## Type '\\disconnect <channel_name>'")
                disconnect(channel)
            elif inp.startswith('\\channel'):
                try:
                    filter = inp.split(' ')[1]
                except:
                    print("## Type '\\channel <channel_name>'")
            elif inp.startswith('\\help'):
                help()
            else:
                print("## Unrecognized command %s. Type `\\help` to see what commands are available." % inp)
        else:
            tracker = publish.send("%s> %s" % (filter, inp), copy=False, track=True)
            tracker.wait(5)
            if not tracker.done:
                print("## Timeout after 5 sec... :P")

    # Sockets terminate implicitly at garbage collection
    # Would be done here otherwise


## Global variables
connections = []
c_lock = Lock()
filter = "buddy"

if __name__ == '__main__':
    main_context = zmq.Context()
    publish = main_context.socket(zmq.PUB)

    port = 5556
    if len(sys.argv) > 1:
        port = sys.argv[1]

    publish.bind("tcp://*:%s" % port)
    print("Local IP:", socket.gethostbyname(socket.gethostname()))
    print("Port:", port)

    io_loop()
