INPUT_FILE_NAME = "day8Input.txt"
accum = 0
lines = [line for line in open(INPUT_FILE_NAME, 'r')]
lineIndex = 0
linesRead = []
line = lines[0].strip().split()
instr, arg = line[0], int(line[1])
while lineIndex < len(lines):
    if lineIndex in [line[0] for line in linesRead]:
        print("PART ONE:", accum)
        break
    line = lines[lineIndex].strip().split()
    instr, arg = line[0], int(line[1])
    linesRead.append((lineIndex, instr, arg))
    if instr == "acc":
        accum += arg
    elif instr == "jmp":
        lineIndex += arg - 1
    lineIndex += 1
if lineIndex >= len(lines):
    print(accum)
# PART TWO BELOW
lineCandidates = [line for line in linesRead if line[1] != "acc" and 
        line[2] != 0 and line[2] != 1]
instrCandidates = []
for candidate in lineCandidates:
    newInstr = "nop" if candidate[1] == "jmp" else "jmp" 
    newLine = "{} {}".format(newInstr, candidate[2])
    newCand = lines[:candidate[0]] + [newLine] + lines[candidate[0]+1:]
    instrCandidates.append(newCand)
for c in instrCandidates:
    lineIndex = 0
    linesRead = []
    line = c[0].strip().split()
    accum = 0
    while lineIndex < len(c):
        if lineIndex in [line[0] for line in linesRead]:
            break
        line = c[lineIndex].strip().split()
        instr, arg = line[0], int(line[1])
        linesRead.append((lineIndex, instr, arg))
        if instr == "acc":
            accum += arg
        elif instr == "jmp":
            lineIndex += arg - 1
        lineIndex += 1
    if lineIndex >= len(c):
        print("PART TWO:", accum)
        break