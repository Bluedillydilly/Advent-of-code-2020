"""

"""

INPUT_FILE_NAME = "day1Input.txt"
TARGET_SUM = 2020

inputData = []
candidates = []

with open(INPUT_FILE_NAME, 'r') as fn:
    for line in fn:
        inputData.append(int(line.strip()))

# PART ONE
print("PART ONE:")
for index1 in range(len(inputData)):
    year1 = inputData[index1]
    for index2 in range(len(inputData)):
        if index1 == index2:
            continue
        year2 = inputData[index2]
        if year1 + year2 == 2020:
            print("Years: {}, {}\nMultiplied {}".format(
                year1, year2, year1*year2))

# PART TWO
print("\nPART TWO:")
for index1 in range(len(inputData)):
    year1 = inputData[index1]
    for index2 in range(len(inputData)):
        if index1 == index2:
            continue
        year2 = inputData[index2]        
        for index3 in range(len(inputData)):
            if index2 == index3:
                continue
            year3 = inputData[index3]
            if year1 + year2 + year3 == 2020:
                print("Years: {}, {}, {}\nMultiplied {}".format(
                    year1, year2, year3, year1*year2*year3))
                exit()

