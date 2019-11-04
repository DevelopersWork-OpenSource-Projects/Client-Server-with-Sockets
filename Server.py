# import packages
from socket import *
import string
import threading
from threading import Thread

class ClientThread(Thread):
    def __init__(self,connectionSocket,soket,server_port):
        threading.Thread.__init__(self)
        self.connectionSocket = connectionSocket
        self.connectionSocket.settimeout(0.565)
        self.soket = soket
        self.server_port = server_port
    def run(self):
        from time import time
        try:
            clientthrdmsg = self.connectionSocket.recv(1024)
        except:
            print("")
        else:
            clientthrdmsg = clientthrdmsg.decode()
            print("Got the Client Request")
            starting = time()
            print(clientthrdmsg)
            if clientthrdmsg.split(' ')[0] != "GET":
                header = b"HTTP/1.1 400 Bad Request\n"
                htmlcontnt = b"<h1>BAD REQUEST</h1>"
            else:
                header = b"HTTP/1.1 200 OK\n"
            try:
                fname = clientthrdmsg.split(' ')[1]
            except:
                print("Garbage Client")
                return
            if fname == '/':
                fname = "index.html"
            else:
                fname = fname.split('/')
                fname = fname[len(fname)-1]
            try:
                fl = open(fname,'rb')
                contnttyp = str(fname.split('.')[1])
                htmlcontnt = fl.read()
            except:
                contnttyp = "text/html"
                header = b"HTTP/1.1 404 Not Found\n"
                htmlcontnt = b"<h1>PAGE NOT FOUND</h1>"
            #Send one HTTP header line into socket
            #Fill in start
            header += b"Host Name: "+str(self.soket.getsockname()).encode()+b" \nPort: "+str(self.server_port).encode()
            header += b" \nConnection: close \nContent-Type: "+contnttyp.encode()+b"; charset=UTF-8 \nSocket Family: "+str(self.soket.family).encode()+b"\n"
            header += b"Socket Type: "+str(self.soket.type).encode()+b" \nProtocol: "+str(self.soket.proto).encode()+b" HTTP \n"
            header += b"Timeout: "+str(self.soket.gettimeout()).encode()+b"\n\n"  
            #Fill in end
            print(header.decode())
            try:
                #Send the content of the requested file to the client
                self.connectionSocket.send(header+htmlcontnt)
                ending = time()
                print("RTT at server: "+str(ending-starting))
                htmlcontnt = header+b"\nRTT at server: "+str(ending-starting).encode()
                self.connectionSocket.send(htmlcontnt)
            finally:
                #Close client socket
                print("Disconnected Client is "+str(self.connectionSocket))
                self.connectionSocket.close()
class ThreadedSocketServer:
    def __init__(self):
        self.soket = socket(AF_INET, SOCK_STREAM)
        self.soket.settimeout(0.565)
        #Prepare a sever socket
        #Fill in start
        self.server_port = 8080
        import sys as system
        if(len(system.argv)==2):
            self.server_port = int(system.argv[1])
        try:
            self.soket.bind(("127.0.0.1",self.server_port))
        except OSError:
            print("Too busy port")
            exit()
        self.soket.listen(10)
        try:
            self.sokettem = socket()
            self.sokettem.bind(("",80))
            self.sokettem.settimeout(0.762)
            self.sokettem.listen()
        except:
            print("")
        print('Ready to serve...')
        self.serverviwer()
        for tr in oldthreads:
            tr.join()
        # close the socket
        self.soket.close()
        #Fill in end

    def serverviwer(self):
        while True:
            oldthreads = []
            savedaddress = []
            #Establish the connection
            contune = False
            self.connectionSocket, addr = False,False
            try:
                self.connectionSocket, addr = self.sokettem.accept()
            except:
                try:
                    self.connectionSocket, addr = self.soket.accept()
                except:
                    contune = True
                    continue
            #Fill in start
            if self.connectionSocket and addr:
                for itr in savedaddress:
                    if itr[1]+12 < addr[1]:
                        nxtkilladdr.append(itr)
                    if addr[1] == itr[1]:
                        contune = True
                        break
                savedaddress.append(addr)
            else:
                continue
            nxtkilladdr = []
            for itr in nxtkilladdr:
                if len(savedaddress)<=itr:
                    continue
                savedaddress.pop(itr)
            if contune:
                continue
            # create and start a thread
            clintthrd = ClientThread(self.connectionSocket,self.soket,self.server_port)
            oldthreads.append(clintthrd)
            clintthrd.start()
            threadsdead = []
            for itr in range(len(oldthreads)):
                if not oldthreads[itr].isAlive():
                    threadsdead.append(itr)
            for itr in threadsdead:
                if len(oldthreads)<=itr:
                    continue
                oldthreads.pop(itr)
            #Fill in end

ThreadedSocketServer()
