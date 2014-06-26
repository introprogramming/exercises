
import sys, time
import zmq, socket
from multiprocessing import Process, Lock
#print zmq.pyzmq_version()


def receive_loop(connect_to):
    global filter
    local_context = zmq.Context()
    subscribe = local_context.socket(zmq.SUB)
    subscribe.setsockopt(zmq.SUBSCRIBE, filter)
    
    try:
        subscribe.connect(connect_to)
    except zmq.error.ZMQError:
        print "Trouble connecting... :P"
        return
    
    while True:
        #print "Awating message..."
        topic, message = subscribe.recv().split()
        
        print topic, '>', message
        time.sleep(0.005)

def connect():
    print "Connect to..."
    address = raw_input("address (ip): ")
    if address == "":
        address = "localhost"
    try:
        port = int(raw_input("port: "))
        connect_to = "tcp://%s:%s" % (address, port)
    except:
        print "Error! Should look like '192.168.0.1 5556'"
        return
    
    recv_process = Process(target=receive_loop, args=(connect_to,))
    recv_process.daemon = True
    recv_process.start()


def help():
    print """
        Commands:
        \\exit\tExits the program
        \\help\tPrints this help
        \\connect\tConnect to another chat client"""

def io_loop():
    help()
    while True:
        input = raw_input()
        if input.startswith('\\'):
            #command
            if input.startswith('\\exit'):
                break
            elif input.startswith('\\connect'):
                connect()
            elif input.startswith('\\help'):
                help()
            else:
                print "Unrecognized command %s. Type `\\help` to see what commands are available." % input
        else:
            #print "Sending", input, "..."
            global filter
            tracker = publish.send("%s %s" % (filter, input), copy = False, track = True)
            tracker.wait(5)
            if tracker.done:
                pass
                #print "Sent message."
            else:
                print "Timeout :P"
    
    # Sockets terminate implicitly at garbage collection


if __name__ == '__main__':
    main_context = zmq.Context()
    publish = main_context.socket(zmq.PUB)
    
    filter = "buddy"
    
    port = 5556
    if len(sys.argv) > 1:
        port = sys.argv[1]
    
    publish.bind("tcp://*:%s" % port)
    print "Local IP:", socket.gethostbyname(socket.gethostname())
    print "Port:", port
    
    io_loop()
