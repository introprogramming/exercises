
import sys, time
import zmq, socket
from multiprocessing import Process, Lock
#print zmq.pyzmq_version()


def receive_loop(connect_to, filter):
    local_context = zmq.Context()
    subscribe = local_context.socket(zmq.SUB)
    subscribe.setsockopt(zmq.SUBSCRIBE, filter)
    
    try:
        subscribe.connect(connect_to)
    except zmq.error.ZMQError:
        print "## Trouble connecting... :P Check if the adress is correct."
        return
    
    while True:
        #print "Awating message..."
        print subscribe.recv()
        time.sleep(0.005)

def start_listener(connect_to):
    global filter
    p = Process(target=receive_loop, args=(connect_to, filter))
    p.daemon = True
    
    c_lock.acquire()
    connections.append( {'process':p, 'channel':filter, 'client':connect_to} )
    c_lock.release()
    
    p.start()

def connect():
    print "Connect to..."
    address = raw_input("address (ip): ")
    if address == "":
        address = "localhost"
    try:
        port = int(raw_input("port: "))
        connect_to = "tcp://%s:%s" % (address, port)
    except:
        print "## Error! Should look like '192.168.0.1 5556'"
        return
    
    start_listener(connect_to)


def help():
    print """
        Commands:
        \\exit\tExits the program
        \\help\tPrints this help
        \\connect\tConnect to another chat client
        \\channel <name>\tSet chat channel to <name>"""

def disconnect(channel):
    c_lock.acquire()
    #print "## Disconnecting from '"+channel+"'..."
    for entry in connections:
        if entry['channel'] != channel:
            continue
        connections.remove(entry)
        entry['process'].terminate()
    c_lock.release()

def io_loop():
    help()
    while True:
        global filter
        input = raw_input()
        if input.startswith('\\'):
            #command
            if input.startswith('\\exit'):
                break
            elif input.startswith('\\connect'):
                connect()
            elif input.startswith('\\disconnect'):
                try:
                    channel = input.split(' ')[1]
                except:
                    print "## Type '\\disconnect <channel_name>'"
                disconnect(channel)
            elif input.startswith('\\channel'):
                try:
                    filter = input.split(' ')[1]
                except:
                    print "## Type '\\channel <channel_name>'"
            elif input.startswith('\\help'):
                help()
            else:
                print "## Unrecognized command %s. Type `\\help` to see what commands are available." % input
        else:
            tracker = publish.send("%s> %s" % (filter, input), copy = False, track = True)
            tracker.wait(5)
            if not tracker.done:
                print "## Timeout after 5 sec... :P"
    
    # Sockets terminate implicitly at garbage collection
    # Would be done here otherwise


connections = []
c_lock = Lock()

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
