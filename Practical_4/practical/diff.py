from utils import diff
import sys


def main(args):
    if len(args) != 2:
        sys.stderr.write(
            'Usage: diff.py <path to old version> <path to new version>\n')
        sys.exit(1)

    for line in diff(args[0], args[1]):
        print(line)


if __name__ == '__main__':

    main(sys.argv[1:])
