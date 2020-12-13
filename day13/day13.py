from math import prod
INPUT_FILE_NAME = "day13.txt"
with open(INPUT_FILE_NAME, 'r') as fn:
    earlyTime = int(fn.readline().strip())
    runningBuses = fn.readline().strip().split(',')
    IDs = [int(id) for id in runningBuses if id != 'x']
    IDtimes = [(id, id - earlyTime%id) for id in IDs]
    IDtimes.sort(key=lambda x: x[1])
    bestBus = IDtimes[0]
    print("PART ONE:", bestBus[0]*bestBus[1])

    offset = 0
    offsets = []
    for bus in runningBuses:
        if bus != 'x':
            offsets.append(int(bus)-offset)
        offset += 1
    product = prod(IDs)
    partialProd = [product//id for id in IDs]
    inv = [pow(partialProd[i],-1,IDs[i]) for i in range(len(IDs))]
    sums = [offsets[i]*partialProd[i]*inv[i] for i in range(len(IDs)) ]
    minTime = sum(sums) % product
    print("PART TWO:", minTime)