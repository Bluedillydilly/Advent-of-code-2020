import re
INPUT_FILE_NAME = "day7Input.txt"
heldBy = {}
target = "shiny gold"
for line in open(INPUT_FILE_NAME, 'r'):
    pattern = "(\w+\s\w+)\sbags\scontain((?:\s\w(?:\s\w+){2}\sbag[s]?[,.])+)?"
    bags = re.findall(pattern, line)[0]
    start = bags[0]
    ends = re.split('\sbag[s]?\s\d\s', re.sub(r'[,.]', '', bags[1].strip()))
    ends[0] = ends[0][2:]
    ends[-1] = re.sub('\sbag[s]?', '', ends[-1])
    for end in ends:
        if not start in heldBy.get(end, []):
            heldBy[end] = heldBy.get(end, []) + [start]
canHoldTarget = []
queue = heldBy[target]
while queue:
    current = queue.pop(0)
    if current in canHoldTarget:
        continue
    parents = heldBy.get(current,[])
    queue += [p for p in parents if not p in canHoldTarget]
    canHoldTarget.append(current)
print("PART ONE:", len(canHoldTarget))

