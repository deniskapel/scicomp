from utils import VersionControl, diff
import os
from time import sleep


def main():
    vc = VersionControl()
    vc.init()
    # test updates
    to_replace = ['111', 'ccc']

    for i in range(2):
        updated = open('new.txt', 'r').readlines()
        outf = open('new.txt', 'w')
        for line in updated:
            line = line.strip()

            if line == to_replace[i]:
                line = '222'

            print('%s' % (line), file=outf)

        outf.close()
        sleep(2)
        vc.add('./new.txt')
        vc.commit('Update new.txt file')

    print('\n\n')
    print(vc)


if __name__ == '__main__':
    main()
