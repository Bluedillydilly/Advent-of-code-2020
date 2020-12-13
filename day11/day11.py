INPUT_FILE_NAME = "day11.txt"
initSeating = {}
empty, occupied, floor = 'L', '#', '.'

for (row, line) in enumerate(open(INPUT_FILE_NAME).read().split()):
    for (col, status) in enumerate(line):
        initSeating[(col,row)] = status

prevSeating, currSeating = {}, initSeating.copy()
def busyNeighCount(spot, seating):
    busy = []
    for x in range(-1+spot[0], 1+spot[0]+1):
        for y in range(-1+spot[1], 1+spot[1]+1):
            if (x,y) == spot:
                continue
            if seating.get((x,y)) == occupied:
                busy.append((x,y))
    return len(busy)
# PART ONE
while prevSeating != currSeating:
    prevSeating = currSeating.copy()
    for spot, seat in currSeating.items():
        if seat == empty:
            if busyNeighCount(spot, prevSeating) == 0:
                currSeating[spot] = occupied
        elif seat == occupied:
            if busyNeighCount(spot, prevSeating) >= 4:
                currSeating[spot] = empty
print("PART ONE:", list(currSeating.values()).count(occupied))

def busyRayCount(spot, seating):
    busyCount = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (x,y) == (0,0):
                continue
            currX, currY = spot[0] + x, spot[1] + y
            currRay = seating.get((currX,currY), False)
            while currRay:
                if currRay == occupied:
                    busyCount += 1
                    break
                elif currRay == empty:
                    break
                currX, currY = currX + x, currY + y
                currRay = seating.get((currX, currY), False)
    return busyCount
# PART TWO
prevSeating, currSeating = {}, initSeating.copy()
while prevSeating != currSeating:
    prevSeating = currSeating.copy()
    for spot, seat in currSeating.items():
        if seat == empty:
            if busyRayCount(spot, prevSeating) == 0:
                currSeating[spot] = occupied
        elif seat == occupied:
            if busyRayCount(spot, prevSeating) >= 5:
                currSeating[spot] = empty
print("PART TWO:", list(currSeating.values()).count(occupied))