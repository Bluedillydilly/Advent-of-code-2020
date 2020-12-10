from math import prod, factorial
INPUT_FILE_NAME = "day10.txt"
volts = [int(line.strip()) for line in open(INPUT_FILE_NAME, 'r')]
volts += [max(volts) + 3] + [0]
order = volts[:]
order.sort()
diff = [order[i+1] - order[i] for i in range(0,len(order)-1)]
print("PART ONE:", diff.count(1)*diff.count(3))
def subDivide(bigList, delimiter):
    g = []
    for diff in bigList:
        if diff == delimiter:
            yield g
            g = []
        g.append(diff)
    yield g
def counts(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return counts(n-1) + counts(n-2) + counts(n-3)
onesLists = list(subDivide(diff, 3))
onesSteps = prod([counts(n) for n in [el.count(1) for el in onesLists] if n>0])
print("PART TWO:", onesSteps)