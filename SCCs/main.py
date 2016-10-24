from DFS import *

from variables import *

import numpy as np

### Main ###

import sys
import threading

sys.settrace

threading.stack_size(67108864)

sys.setrecursionlimit(10000000)

thread = threading.Thread()

thread.start()

G = Edges

print "Computing reverse of graph..."
G_rev = []

for i in range(0, len(G)):
    tail = G[i][0]
    head = G[i][1]
    G_rev.append([head, tail])
    neighbour_rev[head-1].append(tail)
    neighbour[tail-1].append(head)
print "Reverse of graph completed. \nComputing first pass..."

for i in range(n-1, -1, -1):
    if unexplored[i]:
        DFS(G_rev, i)
print "First pass completed."


for i in range(0, len(unexplored)):
    unexplored[i] = 1

print "Starting second pass..."
for i in range(n-1, -1, -1):
    x = finishingOrder[i] - 1
    if unexplored[x]:
        DFS_forw(G, x)
        SCCsSize()

print "Second pass complete."

print "Sorting the array of SCC..."

SCCsList, num_inversions = Mergesort_Inversions(SCCsList)
#SCCsList, num_comparisons = QuickSort(SCCsList, 0, (len(SCCsList)-1))
print "Array sorted, the strongly connected components are:"
print SCCsList
#print "Five largest SCCs:", SCCsList[len(SCCsList)-1], SCCsList[len(SCCsList)-2], SCCsList[len(SCCsList)-3], SCCsList[len(SCCsList)-4], SCCsList[len(SCCsList)-5]

