import re
INPUT_FILE_NAME = "day14.txt"
pattern = r"(?:mem\[(\d*)\]\s=\s(\d*))|(?:mask\s=\s(\w*))"
matches = re.findall(pattern, ''.join(open(INPUT_FILE_NAME, 'r').readlines()))
mask = ''
memValueMask = {}
memAddrMask = {}
for line in matches:
    if line[2]:
        mask = line[2]
    else:
        addr = int(line[0])
        value = int(line[1])
        fixMask = [bit for bit in enumerate(mask) if bit[1]]
        valueBits = list(format(value, '036b'))
        addrBitsList = [list(format(addr, '036b'))]
        for fixBit in fixMask:
            if fixBit[1] != 'X':
                valueBits[fixBit[0]] = fixBit[1]
            if fixBit[1] == '1':
                for addrBits in addrBitsList:
                    addrBits[fixBit[0]] = '1'
            elif fixBit[1] == 'X':
                newAddresses = []
                for addrBits in addrBitsList:
                    newAddr = addrBits[:]
                    newAddr[fixBit[0]] = '1'
                    addrBits[fixBit[0]] = '0'
                    newAddresses.append(newAddr)
                addrBitsList += newAddresses
            elif fixBit[1] == '0': 
                continue
        for addrBits in addrBitsList:
            memAddrMask[int(''.join(addrBits),2)] = value
        memValueMask[addr] = int(''.join(valueBits), 2)
print("PART ONE:", sum(list(memValueMask.values())))
print("PART TWO:", sum(list(memAddrMask.values())))



