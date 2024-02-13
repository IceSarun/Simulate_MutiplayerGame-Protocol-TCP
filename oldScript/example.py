# from socket import *
# import base64

# mailserver = 'mxa-00256a01.gslb.pphosted.com'
# serverPort = 25


# with socket(AF_INET, SOCK_STREAM) as clientSocket:
#     clientSocket.connect((mailserver, serverPort))
#     tcpResponse = clientSocket.recv(1024).decode()
#     print(tcpResponse)

#     # Send handshake.
#     heloCommand = 'HELO Alice\r\n'
#     clientSocket.sendall(heloCommand.encode())
#     heloCommandResponse = clientSocket.recv(1024).decode()
#     print(heloCommandResponse)

#     # FROM 
#     mailFrom = 'MAIL FROM: <icekungza52@gmail.com>\r\n'
#     clientSocket.sendall(mailFrom.encode())
#     mailFromResponse = clientSocket.recv(1024).decode()
#     print("Server Response: " + mailFromResponse)


#     #TO 
#     rcpt = 'RCPT TO: <icesarunpawut3546@gmail.com>\r\n'
#     clientSocket.sendall(rcpt.encode())
#     rcptResponse = clientSocket.recv(1024).decode()
#     print("Server Response: " + rcptResponse)

#     # Send DATA command and print server response.
#     data = 'DATA\r\n'
#     clientSocket.sendall(data.encode())
#     dataResponse = clientSocket.recv(1024).decode()
#     print("Server Response: " + dataResponse)

#     # Send email data.
#     mailD = 'Subject: NEW YEAR Letter \r\n\r\n Happy New Year 2024!'
#     clientSocket.sendall(mailD.encode())

#     # Send message to close email message.
#     endMail = '\r\n.\r\n'
#     clientSocket.sendall(endMail.encode())
#     messageResponse = clientSocket.recv(1024).decode()
#     print("Server Response: " + messageResponse)

#     # Send QUIT command and get server response.
#     quitCommand = 'QUIT\r\n'
#     clientSocket.sendall(quitCommand.encode())
#     quitCommandResponse = clientSocket.recv(1024).decode()
#     print("Server Response: " + quitCommandResponse)

#     clientSocket.close()
#     # import the necessary components first







