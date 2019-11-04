import string
# import socket package
from socket import socket as socketClass

class HTTPClient:        
    def headerbuilder(self,fileloc,socketobj):
        # writes the message for server
        header = "GET "+fileloc+" HTTP/1.1\nHost Name: "+str(socketobj.getsockname())
        header += "\nPort: "+str(socketobj.getsockname()[1])+"\n"
        header += "Socket Family: "+str(socketobj.family)+"\n"
        header += "Socket Type: "+str(socketobj.type)+"\nProtocol: HTTP "+str(socketobj.proto)+"\n"
        header += "Connection: keep-alive\nTimeout: "+str(socketobj.gettimeout())+"\nPeer Name: "+str(socketobj.getpeername())+"\n\n"
        header=header.encode()
        return header
    # client function begins
    def funclnt(self):
        # import time module from time package
        from time import time as timeofinstance
        socketobj = socketClass()
        hostname = "localhost"
        hostport = 8080
        # getting cmd args
        import sys as systemarg
        if len(systemarg.argv) >= 3:
            hostname = str(systemarg.argv[1])
            hostport = int(systemarg.argv[2])
        try:
            socketobj.connect((hostname,hostport))
        except:
            print("Is server running please check")
            exit()
        if len(systemarg.argv) == 4:
            localfile = str(systemarg.argv[3])
        else:
            localfile = str("/index.html")
        header = self.headerbuilder(localfile,socketobj)
        starting = timeofinstance()
        # sending the message
        socketobj.send(header)
        servermesg = socketobj.recv(1024)
        servermesg= servermesg.decode()
        ending = timeofinstance()
        print(servermesg)
        tripofclient = str(ending-starting)
        # timeofinstance time for client displayed
        print("RTT at Client: "+tripofclient)
        filename = str(str(socketobj.getsockname()))
        filesave = open("Downloads/index.html",'w+')
        servermesg = "Round Trip Time: "+tripofclient+" "+servermesg
        filesave.write(servermesg)
        # claosing socket connection and file
        filesave.close()
        socketobj.close()
# creates a object and calls the method
HTTPClient().funclnt()
