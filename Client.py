from socket import AF_INET, SOCK_STREAM, socket
from time import sleep
import smtplib
import os

if __name__ == '__main__':
   
    print('Listening...')
    s = socket(AF_INET, SOCK_STREAM)
    # Producing server socket
    
    print('TCP Socket created')
    server_address = ('127.0.0.1',7770)
    
    s.connect(server_address)
    # Connecting to address
    
    print('socket is connected to %s:%d' % s.getpeername())  
    print('Local end-point is bound to %s:%d' % s.getsockname())
    print('\n Please wait...')
    
   
    EMAIL_ADDRESS = 'wi2101616@gmail.com' 
    EMAIL_PASSWORD = 'WI180360!'
    
    
    #Using context manager to make sure connection is closed automatically 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        
        subject = 'Testing Smtp mail server'
        body = 'It worked :)'
        msg = f'Subject: {subject}   \n\n     {body}'
        
        smtp.sendmail(EMAIL_ADDRESS, 'waleedibrahim882@gmail.com', msg)
        
        #Sending message to email to mail address
        #note message also gets sent to the localsmtp server
        
    print("____________________________________________________________")
    print('')
    
    # Simulaion to show communications between a SMTP client and SMTP Server
    
    # 'Established connection'<<
    print('220 - Service Ready')
    # 'hello' sends back<<
    print('250 - ok')
    # 'Mail from' sends back<<
    print('250 - ok')
    # 'Rcpt to' sends back<<
    print('250 - ok')
    # 'Data' sends back<<
    print('354 - Start mail input')
    # 'Mail transaction' sends back<<
    print('250 - ok')
    # 'quiting...' sends back<<
    print('221 - Connection closed')
  
    print("____________________________________________________________")
    print('')
    
    #Sending data to the server using sendall function
    if s.sendall(msg.encode()) == None:
        print('Send %d bytes to %s:%d' % ((len(msg),)+s.getpeername()))
        
    input('press Enter to terminate....')
    wait_secs = 5
    print('Waiting %d seconds before termination ...' %wait_secs)
    sleep(wait_secs)
    print('Closing the TCP socket...')
    s.close()
    print('terminating....')
