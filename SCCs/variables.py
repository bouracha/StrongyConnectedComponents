class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return len(self.items) == 0


print "Reading Data..."

result_file = r'small_input.txt'
with open(result_file) as file:
    Edges = [[int(digit) for digit in line.split()] for line in file]

n = 0
for x in range(0, len(Edges)):
    if max(Edges[x]) > n:
        n = max(Edges[x])

unexplored = [1] * n
global size
size = 0
SCCsList = []
neighbour_rev = [[None for x in range(0)] for y in range(n)]
neighbour = [[None for x in range(0)] for y in range(n)]

finishingOrder = []
