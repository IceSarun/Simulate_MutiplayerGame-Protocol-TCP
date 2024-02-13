from socket import*
from _thread import *
from player import Player
# สำหรับแปลง object -> byte
import pickle

#set up server (can change)
serverHost = "192.168.1.11"
serverPort = 12500

s = socket(AF_INET, SOCK_STREAM)

try:
    s.bind((serverHost, serverPort))
except error as e:
    str(e)

s.listen(2)
print("Server Started")

players = [Player(200,220,50,25,(255,20,220)), Player(100,100, 50,25, (0,220,255))]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()
    

currentPlayer = 0
while True:
    try:
        conn, addr = s.accept()
        print("Connected to:", addr)

        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1
    except IndexError:
        s.close()
        break

