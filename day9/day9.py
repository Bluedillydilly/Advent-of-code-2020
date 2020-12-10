INPUT_FILE_NAME = "day9.txt"
preamble = 25
startIndex = 0
minCont = 2
target = 0
lines = [int(line.strip()) for line in open(INPUT_FILE_NAME, 'r')]
while True:
    checkNum = lines[preamble+startIndex+1]
    validNum = False
    for prevNum1 in range(startIndex, preamble+startIndex+1):
        for prevNum2 in range(prevNum1+1, preamble+startIndex+1):
            if lines[prevNum1] + lines[prevNum2] == checkNum:
                validNum = True
    if not validNum:
        target = checkNum
        break
    startIndex += 1
print("PART ONE:", target)
candidates, startIndex = [], 0
currIndex = startIndex
while True:
    if sum(candidates) == target and len(candidates) != 1:
        break
    if sum(candidates) > target:
        candidates = []
        startIndex += 1
        currIndex = startIndex
    candidates.append(lines[currIndex])
    currIndex += 1
minCan, maxCan = min(candidates), max(candidates)
print("PART TWO:", minCan+maxCan)