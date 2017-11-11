#create an INET, STREAMing socket
import socket

import sys
from threading import Thread,current_thread

import time

HOST = 'localhost'
PORT = 4444
BUFSIZE = 1024

def run_thread(param):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        clientsocket.connect((HOST,PORT))
        clientsocket.sendall(param)
        # Now receive data
        data = clientsocket.recv(BUFSIZE)
        print ("Client received data as [%s]"%(str(data)))

    except socket.error as nwerror:
        print ("CLIENT socket error!(%s)" % (str(nwerror)))
    finally:
        clientsocket.close()


def wait_for_all_threads_exit(threadList):
    for thread in threadList:
        thread.join(timeout=None)


if __name__ == '__main__':
    try :
        if len(sys.argv) < 2 :
            raise ValueError("Not enough arguments.")

        threadList = []
        threadCount = len(sys.argv)
        print ("thread Count %d"%(threadCount))
        while threadCount > 1:
            thread = Thread(target=run_thread, args=(sys.argv[threadCount-1],))
            thread.start()
            threadCount -= 1
            threadList.append(thread)

        wait_for_all_threads_exit(threadList)

    except Exception as e:
        print (e)





