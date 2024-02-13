# import socket
# from smtplib import *
# import ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # ตั้งค่าพารามิเตอร์
# serverHost = "192.168.1.4"
# serverPort = 19000

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
#     clientSocket.connect((serverHost, serverPort))
#     message = "Hello Server"
#     # message = input("Enter message to Server")
#     clientSocket.sendall(message.encode())
#     data = clientSocket.recv(1024).decode()
#     print(f"Received {data!r}")

#     #set parameter
#     serverPortM = 465
#     smtp_server = "smtp.gmail.com"
#     sender_mail = "icesarunpawut3546@gmail.com"
#     # password = input("Enter your password: ")
#     # test
#     receiver_mail = "sarunpawat.p@ku.th"
#     # receiver_mail = input("TO: ")

#     message = MIMEMultipart("alternative")
#     message["From: "] = sender_mail
#     message["To: "] = receiver_mail
#     message["Subject"] = " New Year Letter"

#     # Create the plain-text
#     text = """\
#     Hello,
#     Happy New Year 2024!
#     โชคดีมีชัย
#     ซินเจียยู่อี่ซินนี้ฮวดไช้
#     """
#     html = """\
#     <html>
#     <body>
#         <p>Hello,<br>
#         Happy New Year 2024!<br>
#         โชคดีมีชัย
#         ซินเจียยู่อี่ซินนี้ฮวดไช้
#         </p>
#     </body>
#     </html>
#     """

#     part1 = MIMEText(text, "plain")
#     part2 = MIMEText(html, "html")
#     message.attach(part1)
#     message.attach(part2)

#     # Create a secure SSL context
#     context = ssl.create_default_context()

#     with SMTP_SSL(smtp_server,serverPortM, context=context) as serverSocket:
#             serverSocket.ehlo()
#             serverSocket.login(sender_mail, password)
#         #     serverSocket.sendmail(
#         #         sender_mail,receiver_mail,message.as_string()
#         # )
#             serverSocket.quit()
#             print('Email sent successfully!')
#     serverSocket.close()
#     clientSocket.close()



