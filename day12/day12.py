from math import sin, cos, pi
from numpy import matmul
INPUT_FILE_NAME = "day12.txt"
direction = { 'N':(0,1), 'E':(1,0), 'S':(0,-1), 'W':(-1,0)}

currDir = 'E'
x,y = 0,0
for line in open(INPUT_FILE_NAME, 'r'):
    command, arg = line.strip()[0], int(line.strip()[1:])
    #print(command, arg)
    if command in direction.keys():
        xVec, yVec = direction[command]
        x += xVec * arg
        y += yVec * arg
    elif command in ['L', 'R']:
        move = -1 if command == 'L' else 1
        move = int(move*arg/90)
        currDirIndex = list(direction.keys()).index(currDir)
        newDirIndex = (currDirIndex + move) % len(direction.keys())
        currDir = list(direction.keys())[newDirIndex]

    elif command == 'F':
        xDir, yDir = direction[currDir]
        x += xDir * arg
        y += yDir * arg
    #print("X:", x, "Y:", y, "FACING:", currDir)
print("PART ONE:", abs(x) + abs(y))

x,y = 0,0
wayX, wayY = 10, 1
for line in open(INPUT_FILE_NAME, 'r'):
    command, arg = line.strip()[0], int(line.strip()[1:])
    #print(command, arg)
    if command in direction.keys():
        xVec, yVec = direction[command]
        wayX += xVec * arg
        wayY += yVec * arg
    elif command in ['L', 'R']:
        move = [[0,1],[-1,0]] if command == 'R' else [[0,-1],[1,0]]
        times = int(arg/90)
        for i in range(times):
            wayX, wayY = matmul(move, [wayX,wayY])
    elif command == 'F':
        x += wayX * arg
        y += wayY * arg
    #print("X:", x, "Y:", y, "Way point:", wayX, wayY)
print("PART TWO:", abs(x) + abs(y))
