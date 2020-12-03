INPUT_FILE_NAME = "day1Input.txt"
TARGET_SUM = 2020
inputData = [int(line.strip()) for line in open(INPUT_FILE_NAME, 'r')]
# PART ONE
print("PART ONE:")
for index1 in range(len(inputData)):
    year1 = inputData[index1]
    for index2 in range(index1 + 1, len(inputData)):
        year2 = inputData[index2]
        if year1 + year2 == 2020:
            print("Years: {}, {}\nMultiplied {}".format(year1, year2, year1*year2))
# PART TWO
print("PART TWO:")
for index1 in range(len(inputData)):
    year1 = inputData[index1]
    for index2 in range(index1 + 1, len(inputData)):
        year2 = inputData[index2]        
        for index3 in range(index2 + 1, len(inputData)):
            year3 = inputData[index3]
            if year1 + year2 + year3 == 2020:
                print("Years: {}, {}, {}\nMultiplied {}".format(
                    year1, year2, year3, year1*year2*year3))