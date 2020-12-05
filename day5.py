INPUT_FILE_NAME = "day5Input.txt"
import re
maxID = 0
for line in open(INPUT_FILE_NAME, 'r'):
    line = line.strip()
    # R, B -> '1'
    # L, F -> '0'
    seatID = re.sub(r'R', '1', re.sub(r'L', '0', re.sub(r'F', '0', re.sub(r'B', '1', line))))
    seatID = int(seatID, 2)
    if seatID > maxID:
        maxID = seatID
print(maxID)