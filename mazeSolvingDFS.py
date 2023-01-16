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

print("Which variant to use? V1 or V2")
variant = str(input())

if variant != "V1" and variant != "V2":
    print("Wrong variant!")
    quit()

nodes = ["[X="+str(startx+1)+",Y="+str(starty+1)+"]"]

print(str(starty) + "x" + str(startx))

trials = 0
global traceText

def isSafe(x, y, board, procedure, L, f):
    global trials
    trials = trials + 1
    global traceText
    if(maze[y][x]==0):
        if(y==0 or y == m-1 or x == 0 or x==n-1):
            traceText += f'{trials: 9}'+") "+"-"*(L-3)+"R"+str(procedure+1)+". U="+str(x+1)+", V="+str(y+1)+". Free. L:=L+1=" + str(L) +". LAB["+str(x+1)+", "+str(y+1)+"]:="+str(L)+". Terminal. \n"
            return True
        else:
            traceText += f'{trials: 9}'+") "+"-"*(L-3)+"R"+str(procedure+1)+". U="+str(x+1)+", V="+str(y+1)+". Free. L:=L+1=" + str(L) +". LAB["+str(x+1)+", "+str(y+1)+"]:="+str(L)+".\n"
            return True
        
    elif(maze[y][x]==1):
        traceText += f'{trials: 9}'+") "+"-"*(L-3)+"R"+str(procedure+1)+". U="+str(x+1)+", V="+str(y+1)+". Wall.\n"

        return False

    traceText += f'{trials: 9}'+") "+"-"*(L-3)+"R"+str(procedure+1)+". U="+str(x+1)+", V="+str(y+1)+". Thread.\n"

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
    result_text += rules[0]
    for i in range(1,len(rules)):
        result_text+=", "+rules[i]
    result_text += "."
    result_text += "\n\t3.3. Nodes: "
    result_text += nodes[0]
    for i in range(1,len(nodes)):
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

    global traceText
    traceText = "\nPart 2. Trace\n\n"
    print(traceText)
    traceText=""
    
	# Checking if solution exists or not
    if(not solveKTUtil(n, maze, startx, starty, move_x, move_y, pos, f)):
        printSolution(False, f)
    else:
        printSolution(True, f)


def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos, f):

    if(curr_x==0 or curr_x==n-1 or curr_y==0 or curr_y==m-1):
        return True

    for i in range(4):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        global traceText
        if(isSafe(new_x, new_y, board, i, pos+1, f)):
            maze[new_y][new_x] = pos+1
            f.write(traceText)
            print(traceText)
            traceText = ""
            rules.append("R"+str(i+1))
            nodes.append("[X="+str(new_x+1)+",Y="+str(new_y+1)+"]")
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1,f)):
  
                return True
            else:

                traceText += " "*11+"-"*(pos-1)+"Backtrack from X="+str(curr_x)+", Y="+str(curr_y)+". L=" +str(pos+1)+". LAB["+str(curr_x)+", "+str(curr_y)+"]:=-1. L:=L-1="+str(pos)+".\n"
                f.write(traceText)
                print(traceText)
                traceText = ""
                rules.pop()
                nodes.pop()
            # Backtracking
            if(variant == "V1"):
                maze[new_y][new_x] = -1
            else:
                maze[new_y][new_x] = 0
        else:
            f.write(traceText)
            print(traceText)
            traceText = ""
    return False


if __name__ == "__main__":



    f = open("out-maze-DFS.txt", "w")

    printFirstPart(f)
    solveKT(n, f)
    f.close()

