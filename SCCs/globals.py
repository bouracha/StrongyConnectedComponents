print "Reading Data..."

result_file = r'small_input.txt'
with open(result_file) as file:
    Edges = [[int(digit) for digit in line.split()] for line in file]