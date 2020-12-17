INPUT = [17,1,3,16,19,0]
short_input = [3,1,2]

starting = INPUT
starting = starting[-1::-1]
iterations = 2020 - len(starting)

while iterations:
    numAge = 0
    if starting[0] in starting[1:]:
        numAge = starting[1:].index(starting[0]) + 1
    starting = [numAge] + starting
    iterations -= 1
print("PART ONE:", starting[0])