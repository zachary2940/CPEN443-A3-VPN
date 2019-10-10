'''
This server waits for conenction from client and displays clients address
TODO: 
1. Encrypt data sent
2. Link to GUI

The program you must create can be toggled between “client mode” and “server mode”. When set in server mode, the program waits for a 
TCP connection on a port that can be specified on the user interface (UI). When set in client mode, the program can initiate a TCP 
connection to a given host name (or IP address), on a given port; both the target host name (IP address) and the TCP port are specified on the UI.
The TA will choose two machines (computer A and computer B), and install one instance of your program on A and another instance on B; both 
instances will then be run, one in client mode and one in server mode, with the client connecting to the server. The TA will input shared secret 
value into “Shared Secret Value” window on both, client and server.
On A, the TA will type some text into a “Data to be Sent” window and then click a “Send” button. On B, the received text will be 
displayed in a “Data as Received” window. Similarly, it should be possible to type data at B and receive/display it at A.
By the time that the TA is ready to type into the “Data to be Sent” window, the two machines must be certain that they
 are talking to each other (i.e., no other machine is impersonating one of them) and must share a fresh symmetric key that no one else knows.
You may choose whichever mutual authentication protocol and whichever key establishment protocol (or whichever combined protocol), stream or 
block ciphers and modes of operation you wish. However, you must be able to defend why you chose it and why you feel it is suitable (i.e., sufficiently
 secure) for implementing a VPN. To keep things simple, appropriate cryptographic algorithms include AES, DES, MD5, SHA (various versions), RSA, D-H, HMAC-MD5; when using these, ignore all padding rules (i.e., when padding is required, pad with zeros) and use the smallest moduli that will work.
Your UI must allow the TA to see what data is actually sent and received over the wire at each point in the setup and communication processes. The TA should be able 
to step through these processes using a “Continue” button.
'''
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# with is constructor and at end of with it is a destructor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #listening at localhost
    s.listen()
    conn, addr = s.accept() # Only if client is run
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024) # Limit message size to 1024 bytes?
            if not data: # At end of message break
                break
            conn.sendall(data) # echos the data TODO change this to a reply