from socket import AF_INET, SOCK_STREAM, socket
from time import sleep
import uuid

if __name__ == '__main__':
    
    print('Application started')
    s = socket(AF_INET, SOCK_STREAM) 
    # Producing client socket
   
    print('TCP Socket created')
    s.bind(('127.0.0.1', 7770))
    # Creating new bound function
   
    print('socket is bound to %s:%d' % s.getsockname())
    backlog = 0 
    s.listen(backlog) 
    #Call specifies a readiness to accept client connection requests.
   
    print('socket is in listening state to %s:%d' % s.getsockname())
    client_socket,client_addr = s.accept() 
    # Accepting incoming connection from client
    
    print('New client connected from %s:%d' % client_addr)
    
    recv_buffer_length = 1024
    msg = client_socket.recv(recv_buffer_length) #Recieve message from client
 
    print('Recieved %d bytes from %s:%d' % ( (len(msg),)+client_addr))
    # Calculating bytes recieved 
    
    print('Received message: \n%s' %msg) 
    # Print message from client 
    
    to = 'wi2101616@gmail.com' 
    From = 'waleedibrahim882@gmail.com'
    domain = 'gmail.com'
    
    print("____________________________________________________________")
    print('')
   
    # Simulaion to show communications between a SMTP client and SMTP Server
    
    print('Established connection')
    # '220 - Service Ready' >>
    print('250 - hello', domain)
    # '250 - ok' >>
    print('Mail from:', From)
    # '250 - ok' >>
    print('Rcpt to', to)
    # '250 - ok' >>
    print('Data')
    # '354 - Start mail input' >>
    print('Mail transaction')
    # '250 - ok' >>
    print('Quit')
    # '221 - Connection closed' >>
    
    print("____________________________________________________________")
    print('')
    
    # Importing socket module
    import socket  
    # Using socket.gethostname() to get the hostname socket.gethostname() 
    hostname = socket.gethostname()
    # Using socket.gethostbyname() to get the IP address 
    ip_address = socket.gethostbyname(hostname)
    
    # printing the hostname and ip_address
    print(f"Hostname: {hostname}") 
    print(f"IP Address: {ip_address}")
    print("This is your Mac address: ", end="")
    # Joins elements of getnode() after each 2 digits (geeksforgeeks,2021)
    print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1])) 
    
    msg = (ip_address)

    input('press Enter to terminate....')
    wait_secs = 5
    print('Waiting %d seconds before termination ...' %wait_secs)
    sleep("wait_secs")
    print('Closing the TCP socket...')
    s.close()
    print('terminating....')
