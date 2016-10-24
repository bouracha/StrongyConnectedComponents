from variables import *


def DFS_iter(G, i):
    s = Stack()
    time_s = Stack()
    s.push(i)
    time_s.push(i)
    while 1:
        v = s.pop()
        #unexplored[v] = 0
        for j in range(0, len(neighbour_rev[v])):
            w = neighbour_rev[v][j] - 1
            if unexplored[w]:
                unexplored[w] = 0
                s.push(w)
                time_s.push(w)
        if s.isEmpty():
            break
    while 1:
        finishingOrder.append(time_s.pop())
        if time_s.isEmpty():
            break


def DFS_iter_forw(G, i):
    global size
    s = Stack()
    s.push(i)
    while 1:
        v = s.pop()
        #unexplored[v] = 0
        for j in range(0, len(neighbour[v])):
            w = neighbour[v][j] - 1
            if unexplored[w]:
                unexplored[w] = 0
                s.push(w)
        if s.isEmpty():
            break
        size += 1


def DFS(G, i):
    unexplored[i] = 0
    for j in range(0, len(neighbour_rev[i])):
        v = neighbour_rev[i][j]-1
        if unexplored[v]:
            DFS(G, v)
    #print "Explored:", i+1
    finishingOrder.append(i+1)

def DFS_forw(G, i):
    global size
    size += 1
    unexplored[i] = 0
    for j in range(0, len(neighbour[i])):
        v = neighbour[i][j]-1
        if unexplored[v]:
            DFS_forw(G, v)
    #print "Explored:", i+1

def SCCsSize():
    global size
    SCCsList.append(size)
    size = 0





def Mergesort_Inversions(A):
    n = len(A)
    if (n == 1):
        return A, 0
    else:
        #print "Splitting: ", A, " into:"
        mid = len(A)//2
        B = A[:mid] ##lefthalf array
        C = A[mid:] ##righthalf array
        #print B
        #print C
        B, x = Mergesort_Inversions(B)
        C, y = Mergesort_Inversions(C)
        D, z = CountSplitInversions(B, C)

        return D, (x+y+z)


def CountSplitInversions(B, C):
    i = j = 0
    num_inversions = 0
    D = []
    #print "Count inversions between:", B, C
    while i < len(B) and j < len(C):
        if (B[i] <= C[j]) and (i < len(B)):
            D.append(B[i])
            i += 1
        elif B[i] > C[j]:
            D.append(C[j])
            #print "Inversion(s) Found!"
            num_inversions += len(B) - (i)
            j += 1

    while i == len(B) and j < len(C):
        D.append(C[j])
        j += 1

    while i < len(B) and j == len(C):
        D.append(B[i])
        i += 1

    #print "Return sorted: ", D, " with ", num_inversions, " inversion"
    return D, num_inversions