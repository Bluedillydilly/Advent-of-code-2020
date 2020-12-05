import re
INPUT_FILE_NAME = "day4Input.txt"
fn = "".join(open(INPUT_FILE_NAME, 'r').readlines())
no_cid = "((?:[^c][a-z]{2}:[#]{0,1}[a-z0-9]*\s){7})"
cid = "((?:[a-z]{3}:[#]{0,1}[a-z0-9]*\s){8})"
pattern = no_cid + "|" + cid
passMatches = [match[0].strip() if match[0] else match[1].strip() for match in re.findall(pattern, fn)]
print("PART ONE: proper formatted passports:", len(passMatches))
birthYear = "(?:byr:(?:(?:19[2-9][0-9])|(?:200[0-2]))\s)"
issueYear = "(?:iyr:20(?:20|1[0-9])\s)"
expireYear = "(?:eyr:20(?:(?:2[0-9])|30)\s)"
height = "(?:hgt:(?:(?:(?:1(?:(?:[5-8][0-9])|(?:9[0-3]))cm))|(?:(?:(?:59)|(?:6[0-9])|(?:7[0-6]))in))\s)"
hairColor = "(?:hcl:#[0-9a-z]{6}\s)"
eyeColor = "(?:ecl:(?:amb|blu|brn|gry|grn|hzl|oth)\s)"
passportID = "(?:pid:[0-9]{9}\s)"
countryID = "(?:cid:[0-9a-z]*\s)"
patternCid = birthYear+"|"+issueYear+"|"+height+"|"+hairColor+"|"+eyeColor+"|"+passportID+"|"+expireYear+"|"+countryID
patternCid = "(?:" + patternCid + "){8}"
patternNoCid = birthYear+"|"+issueYear+"|"+height+"|"+hairColor+"|"+eyeColor+"|"+passportID+"|"+expireYear
patternNoCid = "(?:" + patternNoCid + "){7}"
pattern = patternCid+"|"+patternNoCid
#pattern = patternCid
print(pattern)
matches2 = re.findall(pattern, fn)
print("PART TWO: valid passports:", len(matches2))