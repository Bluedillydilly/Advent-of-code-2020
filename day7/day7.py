import re
INPUT_FILE_NAME = "day7Input.txt"
helds = {}
contains = {}
target = "shiny gold"
for line in open(INPUT_FILE_NAME, 'r'):
    pattern = "(\w+\s\w+)\sbags\scontain((?:\s\w(?:\s\w+){2}\sbag[s]?[,.])+)?"
    bags = re.findall(pattern, line)[0]
    start = bags[0]
    ends = re.split('\sbag[s]?\s', re.sub(r'[,.]', '', bags[1].strip()))
    ends[-1] = " ".join(ends[-1].split(" ")[:-1])
    for end in ends:
        if not end.split(" ")[0]:
            continue
        count = int(end.split(" ")[0]) 
        color = " ".join(end.split(" ")[1:])
        if not start in helds.get(end, []):
            helds[color] = helds.get(color, []) + [start]
    for end in ends:
        
        if end == '':
            contains[start] = contains.get(start, [('', 0)]) 
            pass
        else:
            count = int(end.split(" ")[0]) 
            color = " ".join(end.split(" ")[1:])
            contains[start] = contains.get(start, []) + [(color, count)]
canHoldTarget = []
queue = helds[target]
while queue:
    current = queue.pop(0)
    if current in canHoldTarget:
        continue
    parents = helds.get(current,[])
    queue += [p for p in parents if not p in canHoldTarget]
    canHoldTarget.append(current)
print("PART ONE:", len(canHoldTarget))
def getBags(current):
    if current == '':
        return 1
    children = contains.get(current, '')
    return sum([child[1] + child[1]*getBags(child[0]) for child in children])
totalBags = getBags(target)
print("PART TWO:", totalBags)
