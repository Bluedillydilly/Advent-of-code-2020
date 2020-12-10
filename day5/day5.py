INPUT_FILE_NAME = "day5Input.txt"
import re
maxID, IDlist = 0, []
for line in open(INPUT_FILE_NAME, 'r'):
    seatID = int(re.sub(r'[LF]', '0', re.sub(r'[RB]', '1', line.strip())), 2)
    if seatID > maxID:
        maxID = seatID
    IDlist.append(seatID)
print("PART ONE:", maxID)
IDlist.sort()
print("PART TWO:")
for index in range(len(IDlist)-1):
    if IDlist[index] - IDlist[index+1] == -2:
        print(IDlist[index]+1)