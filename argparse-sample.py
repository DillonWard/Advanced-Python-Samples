import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a,b = b, a + b
    return a

def Main():
    # used for adding an argument when you run the python file
    # initiailizes the argument parser
    parser = argparse.ArgumentParser()

    # adding a mutually exclusive group argument to the parser - select one or the other but not both
    group = parser.add_mutually_exclusive_group()
    # adding arguments to the group arguments
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    # the file is expecting a 'num' argument which is of type 'int'
    # includes a "helper" function if the user types -h as an argument
    parser.add_argument("num", help="The fibonacci number you wish to calculate.", type=int)
    # adds an argument for outputting the result to a file
    parser.add_argument("-o", "--output", help="Output result to a file", action="store_true")
    # sets the args as as the parser with it's arguments
    args = parser.parse_args()
    # sets the result to be what's returned from the argument entered being passed into the 'fib' function
    result = fib(args.num)
    # else if for the output depending on the choice
    if args.verbose:
        # prints out the result as a string
        print("The " + str(args.num) + "th fib number is " + str(result))
    elif args.quiet:
        print(result)
    else:
        print("Fib("+str(args.num)+") = "+str(result))

    if args.output:
        # opens a text file 'fibonacci.txt' in append mode
        f = open("fibonacci.txt", "a")
        # writes to the file and closes it
        f.write(str(result) + '\n')
        f.close()


if __name__ == '__main__':
    Main()