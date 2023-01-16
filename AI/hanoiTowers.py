
# Driver code
print("How many disks?")
N = int(input())

A = [i for i in range(1,N+1)] 
B = []
C = []
step = 0


def TowerOfHanoi(n, from_rod, aux_rod, to_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod,to_rod, aux_rod)
    if from_rod == 'A': A.remove(n)
    elif from_rod == 'B': B.remove(n)
    else: C.remove(n)

    if to_rod == 'A': A.append(n)
    elif to_rod == 'B': B.append(n)
    else: C.append(n)
    
    global step
    step = step +1

    print(f'{step: 5}.',"Move disk", n, "from rod", from_rod, "to rod", to_rod, "\t |    \tA=",A, "B=",B, "C=",C)
    TowerOfHanoi(n-1, aux_rod, from_rod, to_rod)
 
 
if N>10 or N<1:
    print("Wrong number")
else:
    # A, C, B are the name of rods
    print("Initial state:","A=",A, "B=",B, "C=",C )

    TowerOfHanoi(N, 'A', 'B', 'C')