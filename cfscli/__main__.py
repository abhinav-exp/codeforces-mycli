import sys

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    print("This is the command line tool for testing and submiting codeforces solution")



if __name__ == '__main__':
    main()