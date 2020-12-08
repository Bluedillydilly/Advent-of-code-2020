INPUT_FILE_NAME = "day6Input.txt"
from string import ascii_lowercase
fn = open(INPUT_FILE_NAME, 'r').read().strip()
fn = fn.split("\n\n")
qCount = sum( [ len(set(person.replace("\n", ''))) for person in fn ] )
print("PART ONE:", qCount)
sameGroup = [list(set(person.split("\n"))) for person in fn]
sameCount = sum([len(set.intersection(*map(set,group))) for group in sameGroup])
print("PART TWO:", sameCount)

