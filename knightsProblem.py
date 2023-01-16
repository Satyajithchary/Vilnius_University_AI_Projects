# Python3 program to solve Knight Tour problem using Backtracking

# Chessboard Size
print("What is the board size (n)?")
n = int(input())
print("What is the starting X position?")
startx = int(input())
print("What is the starting Y position??")
starty = int(input())

trials = 0

def isSafe(x, y, board, procedure, L, f):
    global trials
    trials = trials + 1
    if(x>=1 and y >= 1 and x <= n and y <= n):
        if (board[x][y] == 0):
            f.write(f'{trials: 9}'+") "+"-"*(L-2)+"R"+str(procedure+1)+". U="+str(x)+", V="+str(y)+", L=" + str(L) +". Free. Board[" + str(x)+","+ str(y)+"]:="+str(L)+".\n")
            return True
        else:
            f.write(f'{trials: 9}'+") "+"-"*(L-2)+"R"+str(procedure+1)+". U="+str(x)+", V="+str(y)+", L=" + str(L) +". THREAD.")
    else:
        f.write(f'{trials: 9}'+") "+"-"*(L-2)+"R"+str(procedure+1)+". U="+str(x)+", V="+str(y)+", L=" + str(L) +". Out.")
    if(procedure==7):
        f.write("Backtrack.")
    f.write("\n")
    return False



def printSolution(tour_boolean, f, n, board):
    result_text = ""
    result_text= result_text + ("\nPart 3.  Results \n")
    if tour_boolean:
        result_text= result_text + ("\t 1) Path is found. Trials="+str(trials)+".\n")
        result_text= result_text + ("\t 2) Path graphically:\n\n")
        result_text= result_text + ("\t Y,  V ^ \n")
        for i in range(n, 0, -1):
            result_text= result_text + ("\t   "+f'{i: 3}'+" | ")
            for j in range(1, n+1):
                result_text= result_text + (f'{board[j][i]: 3}'+" ")
            result_text= result_text + ("\n")
        result_text= result_text + ("\t       "+"-"*(n*4+3)+">  X, U\n")
        result_text= result_text + ("\t         ")
        for i in range(1, n+1):
            result_text= result_text + (f'{i: 3}'+" ")
    else:
        result_text= result_text + ("\t 1) No tour. Trials="+str(trials)+".\n")
    f.write(result_text)
    print(result_text)
    f.close()
    f = open("out-short.txt", "a")
    f.write(result_text)
    f.close()



def solveKT(n, f):
	'''
		This function solves the Knight Tour problem using
		Backtracking. This function mainly uses solveKTUtil()
		to solve the problem. It returns false if no complete
		tour is possible, otherwise return true and prints the
		tour.
		Please note that there may be more than one solutions,
		this function prints one of the feasible solutions.
	'''

	# Initialization of Board matrix
	board = [[0 for i in range(n+1)]for i in range(n+1)]

	# move_x and move_y define next move of Knight.
	# move_x is for next value of x coordinate
	# move_y is for next value of y coordinate
	move_x = [2, 1, -1, -2, -2, -1, 1, 2]
	move_y = [1, 2, 2, 1, -1, -2, -2, -1]

	# Since the Knight is initially at the first block
	board[startx][starty] = 1

	# Step counter for knight's position
	pos = 1

    
	# Checking if solution exists or not
	if(not solveKTUtil(n, board, startx, starty, move_x, move_y, pos, f)):
		printSolution(False, f, n, board)
	else:
		printSolution(True, f, n, board)


def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos, f):
	'''
		A recursive utility function to solve Knight Tour
		problem
	'''

	if(pos == n**2):
		return True

	# Try all next moves from the current coordinate x, y
	for i in range(8):
		new_x = curr_x + move_x[i]
		new_y = curr_y + move_y[i]
		if(isSafe(new_x, new_y, board, i, pos+1, f)):
			board[new_x][new_y] = pos+1
			if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1,f)):
				return True

			# Backtracking
            
			board[new_x][new_y] = 0
	return False


if __name__ == "__main__":

    if(startx <= 0 or startx > n or starty > n or starty <=0 ):
        print("Illegal start (out of board)")
    elif (n<1 or n>10):
        print("Wrong board size")
    else:

        f = open("out-long.txt", "w")
        part_1_text = ""
        part_1_text = part_1_text + ("Part 1.  Data \n")
        part_1_text = part_1_text + ("\t 1) Board: "+str(n)+"x"+str(n)+"\n")
        part_1_text = part_1_text + ("\t 2) Initial position: X="+str(startx)+", Y="+str(starty)+", L=1.\n")
        f.write(part_1_text)
        f.write("\nPart 2.  Trace \n")
        f.close()
        print(part_1_text)
        f = open ("out-short.txt", "w")
        f.write(part_1_text)
        f.close()
        f = open("out-long.txt", "a")
        solveKT(n, f)

