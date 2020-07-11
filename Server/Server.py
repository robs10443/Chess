import socket
import Header_Manager as hm
import threading

soc = socket.socket()

port = 12345

soc.bind(('',port))

soc.listen(5)

print("Server Started")

connections_list = []

def acceptConnections():
    while True:
        conn,_ = soc.accept()
        connections_list.append(conn)
        print ("Player connected")
        if (len(connections_list) > 1):
            t1 = threading.Thread(target=createGame,args=(connections_list[0],connections_list[1]))
            t1.setDaemon(False)
            t1.start()
            connections_list.pop(0)
            connections_list.pop(0)
    

def createGame(player1,player2):
    print('Game Started')
    player1.send('White'.encode('utf-8'))
    
    player2.send('Black'.encode('utf-8'))
    
    game = True
    
    while game:
        msg = player1.recv(1024).decode('utf-8')
        
        if(len(msg) == 1):
            player2.send('2'.encode('utf-8'))
            break
        if(int(msg[0]) == 0):
            flag,starting_row,starting_col,ending_row,ending_col,move,promotion = hm.convertData(msg)

            starting_row = 7 - starting_row
            ending_row = 7 - ending_row

            starting_col = 7 - starting_col
            ending_col = 7 - ending_col

            player2.send(hm.convertDataToHeader(flag,starting_row,starting_col,ending_row,ending_col,move,promotion).encode('utf-8'))
        else:
            player2.send(msg.encode('utf-8'))
            game = False
            break

        msg = player2.recv(1024).decode('utf-8')
        if(len(msg) == 1):
            player1.send('2'.encode('utf-8'))
            break
        if(int(msg[0]) == 0):
            flag,starting_row,starting_col,ending_row,ending_col,move,promotion = hm.convertData(msg)

            starting_row = 7 - starting_row
            ending_row = 7 - ending_row

            starting_col = 7 - starting_col
            ending_col = 7 - ending_col
            

            player1.send(hm.convertDataToHeader(flag,starting_row,starting_col,ending_row,ending_col,move,promotion).encode('utf-8'))
        else:
            player1.send(msg.encode('utf-8'))
            game = False
            break
    print("Game Ended")        
        
acceptConnections()