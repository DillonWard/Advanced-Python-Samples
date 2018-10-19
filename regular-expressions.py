import re

def Main():
    # the line to test
    line = "I think I understand regular expressions"

    # checks for the whole string - think does not match the whole string so will not find it
    matchResult = re.match('think', line, re.M|re.I)

    # if it's found print this
    if matchResult:
        print("Match found: " + matchResult.group())
    else:
        print("No match was found")
    
    # searches for the single word 'think' in the string
    searchResult = re.search("think", line, re.M|re.I)
    # if it's found print this
    if searchResult:
        print("Search found: " + searchResult.group())
    else:
        print("Nothing found in search")

if __name__ == '__main__':
    Main()
    