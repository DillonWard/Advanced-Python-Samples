import re, argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="Specify word to search for")
    parser.add_argument("fname", help="Specify file to search")
    args = parser.parse_args()

    searchFile = open(args.fname)
    lineNum = 0

    for line in searchFile.readlines():
        # ignore new lines
        line = line.strip('\n\r')
        lineNum += 1
        # re.I ignore lines and re.M makes it match the start and end of the line
        searchResult = re.search(args.word, line, re.M|re.I)
        if searchResult:
            print(str(lineNum) + ": " + line)

if __name__ == '__main__':
    Main()