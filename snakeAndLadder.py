import random 

board=[]
for i in range(100):
    board.append(i)

board[6]=38
board[20]=42
board[51]=67

board[17]=7
board[62]=19
board[95]=75

print(board)

pos1=0
pos2=0
while True:
    if pos1==99:
        print("Player1 won!!!")
        break
    elif pos2==99:
        print("player2 won!!!")
        break
    else:
        try:
            dice=int(random.randint(1,6))
            pos1=board[pos1+dice]
            dice=int(random.randint(1,6))
            pos2=board[pos2+dice]

            print(pos1,pos2)
        except:
            pass
