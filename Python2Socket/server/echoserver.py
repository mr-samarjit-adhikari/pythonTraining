import socket
from threading import Thread

import sys

HOST = ''
PORT = 4444
BUFSIZE = 1024
SERVER_STR = "[SERVER ECHO]"

def execute_single_thread(clientsocket, clientaddr):
    thread = Thread(target=single_thread_run, args=(clientsocket, clientaddr))
    thread.start()

def single_thread_run(clientsocket, clientaddr):
    while True:
        try:
            data = clientsocket.recv(BUFSIZE)
            print ("Received data from client [%s] is [%s]"%(clientaddr,data))
            if not data:
                print ("Client [%s] closed connection"%(clientaddr))
                break;
            clientsocket.send(SERVER_STR+str(data));
            #Now echo back to the client
        except socket.error as recverror:
            print ("RW socket error!(%s).Closing ...." % (str(recverror)))
            break;

        finally:
            clientsocket.close()


if __name__=='__main__':

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((HOST,PORT))
    serversocket.listen(5)

    while True:
        try:
            print ("Waiting for new connection ....")
            (clientsocket,clientaddr) = serversocket.accept()
            print ("Client connnected with address %s" % (str(clientaddr)))
            execute_single_thread(clientsocket, clientaddr)

        except socket.error as nwerror:
            serversocket.close()
            print ("LISTEN socket error!(%s)"%(str(nwerror)))
            sys.exit(nwerror.errno)

        except Exception as error:
            print ("EXCEPTION:%s"%(error))
            sys.exit(1)



