board=[[0, 1, 0],[0,0,0],[0,0,0]]
print (len(board))
nX=0
nO=0
for row in board:
    for column in row:
        if (column==0):
            nX=nX+1
        elif (column==1):
            nO=nO+1
print (nX,nO)