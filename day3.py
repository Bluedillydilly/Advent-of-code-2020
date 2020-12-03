import math
INPUT_FILE_NAME = "day3Input.txt"
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
tree_counts = []
TREE_CHAR = '#'
def checkSlope(slope):
    with open(INPUT_FILE_NAME, 'r') as fn:
        temp_tree_count = 0
        checkerWidth = len(fn.readline().strip())
        index = 0
        line = fn.readline()
        while line:
            index = (index + slope[0]) % checkerWidth
            if slope[1] == 2:
                line = fn.readline()
            char = line[index]
            if char == TREE_CHAR:
                temp_tree_count += 1
            line = fn.readline()
    return temp_tree_count
print("Part One:", checkSlope(slopes[1]))
print("Part Two:", math.prod([checkSlope(slope) for slope in slopes]))