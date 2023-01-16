# Chessboard Size
print("Which maze file to solve?")
file = str(input())

with open(file, 'r') as f:
    data = f.read().splitlines()

global maze
maze = [[int(num) for num in line.split(' ')] for line in data[:-1]]
start = data[len(data)-1].split(' ')

rules = []

m = len(maze)
n = len(maze[0])

startx = int(start[0])-1
starty = int(start[1])-1


nodes = ["[X="+str(startx+1)+",Y="+str(starty+1)+"]"]

print(str(starty) + "x" + str(startx))
maze[starty][startx] = 2

trials = 0
FX = []
FY = []
CLOSE = 0
NEWN = 1
YES = False
WAVES =1
global traceText

def isSafe(x, y, board, procedure, L, f):
    global trials, NEWN
    trials = trials + 1
    global traceText
    if(maze[y][x]==0):
        if(y==0 or y == m-1 or x == 0 or x==n-1):
            traceText += "\t\t"+"R"+str(procedure+1)+". X="+str(x+1)+", Y="+str(y+1)+". Free. NEWN="+str(NEWN+1)+". Terminal. \n"
            return True
        else:
            traceText += "\t\t"+"R"+str(procedure+1)+". X="+str(x+1)+", Y="+str(y+1)+". Free. NEWN="+str(NEWN+1)+". \n"
            return True
        
    elif(maze[y][x]==1):
        traceText += "\t\t"+"R"+str(procedure+1)+". X="+str(x+1)+", Y="+str(y+1)+". Wall.\n"

        return False

    traceText += "\t\t"+"R"+str(procedure+1)+". X="+str(x+1)+", Y="+str(y+1)+". Close or new.\n"

    return False

def printFirstPart(f):
    result_text = ""
    result_text= result_text + ("\nPart 1.  Data \n \t1.1. Labyrinth\n")
    result_text= result_text + ("\t Y,  V ^ \n")
    for i in range(m, 0, -1):
        result_text= result_text + ("\t   "+f'{i: 4}'+" | ")
        for j in range(0, n):
            result_text= result_text + (f'{maze[i-1][j]: 4}'+" ")
        result_text= result_text + ("\n")
    result_text= result_text + ("\t        "+"-"*(n*5+3)+">  X, U\n")
    result_text= result_text + ("\t          ")
    for i in range(1, n+1):
        result_text= result_text + (f'{i: 4}'+" ")
    result_text += ("\n\n\t1.2. Initial position X="+str(startx+1)+", Y="+str(starty+1)+". L=2\n\n")
    f.write(result_text)
    print(result_text)


def printSolution(tour_boolean, f):
    result_text = ""
    result_text= result_text + ("\nPart 3.  Results\n")
    if(tour_boolean):
        result_text += "\t3.1. Path is found.\n\t3.2. Path graphically:\n"
    result_text= result_text + ("\t Y,  V ^ \n")
    for i in range(m,0,-1):
        result_text= result_text + ("\t   "+f'{i: 4}'+" | ")
        for j in range(0, n):
            result_text= result_text + (f'{maze[i-1][j]: 4}'+" ")
        result_text= result_text + ("\n")
    result_text= result_text + ("\t        "+"-"*(n*5+3)+">  X, U\n")
    result_text= result_text + ("\t          ")
    for i in range(1, n+1):
        result_text= result_text + (f'{i: 4}'+" ")
    result_text += "\n\n\t3.3. Rules: "
    result_text += rules[len(rules)-1]
    for i in range(len(rules)-2,-1,-1):
        result_text+=", "+rules[i]
    result_text += "."
    result_text += "\n\t3.3. Nodes: "
    result_text += nodes[0]
    for i in range(len(nodes)-1,0,-1):
        result_text+=", "+nodes[i]
    result_text += ".\n"
    f.write(result_text)
    print(result_text)
    # f.close()
    # f = open("out-short.txt", "a")
    # f.write(result_text)
    # f.close()



def solveKT(n, f):

    move_x = [-1, 0, 1, 0]
    move_y = [0, -1, 0, 1]

    pos = 2
    maze[starty][startx] = pos

    FX.append(startx)
    FY.append(starty)

    global traceText
    traceText = "\nPart 2. Trace\n\n"
    print(traceText)
    traceText=""
    
	# Checking if solution exists or not
    if(not solveKTUtil(n, maze, startx, starty, move_x, move_y, pos, f)):
        printSolution(False, f)
    else:
        printSolution(True, f)

def back(y, x, move_x, move_y):

    while(maze[y][x]> 2):
        for i in range(3,-1, -1):
            new_y = y + move_y[i]
            new_x = x + move_x[i]
            
            if (new_y >= 0) and (new_y <= m-1) and (new_x >= 0) and (new_x <= n-1):
                if maze[new_y][new_x] == maze[y][x] - 1:
                    if i <= 1:
                        rules.append("R"+str(i+3))
                    else: 
                        rules.append("R"+str(i-1))
                    nodes.append("[X="+str(x+1)+",Y="+str(y+1)+"]")
                    x = new_x
                    y = new_y
                    break
            

def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos, f):
    global YES, FX, FY, CLOSE, NEWN, traceText, WAVES
    if(curr_x==0 or curr_x==n-1 or curr_y==0 or curr_y==m-1):
        YES = True

    while YES == False or CLOSE > NEWN:
        X = FX[CLOSE]
        Y = FY[CLOSE]
        #print("WAVE "+str(WAVES)+", POS " + str(maze[Y][X]))
        if(maze[Y][X]>WAVES):
            WAVES +=1
            print("WAVE "+str(WAVES-1)+", label L=\""+str(WAVES+1)+"\"\n\tClose CLOSE="+str(CLOSE+1)+", X="+str(X)+", Y="+str(Y)+".")
            f.write("\nWAVE "+str(WAVES-1)+", label L=\""+str(WAVES+1)+"\"\n\tClose CLOSE="+str(CLOSE+1)+", X="+str(X)+", Y="+str(Y)+".\n")
        else:
            print("\tClose CLOSE="+str(CLOSE+1)+", X="+str(X)+", Y="+str(Y)+".")
            f.write("\tClose CLOSE="+str(CLOSE+1)+", X="+str(X)+", Y="+str(Y)+".\n")
        for i in range(4):
            new_x = X + move_x[i]
            new_y = Y + move_y[i]

            if(isSafe(new_x, new_y, board, i, pos+1, f)):
                maze[new_y][new_x] = maze[Y][X] + 1
                # f.write(traceText)
                # print(traceText)
                # traceText = ""
                # rules.append("R"+str(i+1))
                # nodes.append("[X="+str(new_x+1)+",Y="+str(new_y+1)+"]")
                if(new_x==0 or new_x==n-1 or new_y==0 or new_y==m-1):
                    YES = True
                    print(traceText)
                    f.write(traceText)
                    traceText=""
                    back(new_y, new_x, move_x, move_y)
                    break
                else:
                    NEWN += 1
                    FX.append(new_x)
                    FY.append(new_y)
                    # traceText += " "*11+"-"*(pos-1)+"Backtrack from X="+str(curr_x)+", Y="+str(curr_y)+". L=" +str(pos+1)+". LAB["+str(curr_x)+", "+str(curr_y)+"]:=-1. L:=L-1="+str(pos)+".\n"
                    # f.write(traceText)
                    # print(traceText)
                    # traceText = ""
                    # rules.pop()
                    # nodes.pop()
            # else:
                
                # f.write(traceText)
                # print(traceText)
                # traceText = ""
            print(traceText)
            f.write(traceText)
            traceText=""
        CLOSE += 1
        pos += 1
    return YES
        
            


if __name__ == "__main__":



    f = open("out-maze-BFS.txt", "w")

    printFirstPart(f)
    solveKT(n, f)
    f.close()