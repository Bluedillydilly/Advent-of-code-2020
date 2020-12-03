INPUT_FILE_NAME = "day2Input.txt"
inputData = []
correctPass = []
correctCount = 0
part2Count = 0
with open(INPUT_FILE_NAME, 'r') as fn:
    for line in fn:
        splitLine = line.strip().split(" ")
        letCountsSplit = splitLine[0].split("-")
        minLetCount = int(letCountsSplit[0])
        maxLetCount = int(letCountsSplit[1])
        letter = splitLine[1][0]
        letCount = splitLine[2].count(letter)
        # PART ONE
        if minLetCount <= letCount <= maxLetCount:
            correctCount += 1
            correctPass.append(line)
        # PART TWO
        firstLet = splitLine[2][minLetCount-1]
        secondLet = splitLine[2][maxLetCount-1]
        if firstLet != secondLet and (letter == firstLet or letter == secondLet):
            part2Count += 1
    print("Part 1: {}".format(correctCount))
    print("Part 2:", part2Count)