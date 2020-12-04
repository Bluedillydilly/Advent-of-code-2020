import re
INPUT_FILE_NAME = "day4Input.txt"
fn = "".join(open(INPUT_FILE_NAME, 'r').readlines())
no_cid = "((?:[^c][a-z]{2}:[#]{0,1}[a-z0-9]*\s){7})"
cid = "((?:[a-z]{3}:[#]{0,1}[a-z0-9]*\s){8})"
pattern = no_cid + "|" + cid
passMatches = [match[0].strip() if match[0] else match[1].strip() for match in re.findall(pattern, fn)]
print(passMatches)
print("PART ONE:", len(passMatches))
