import os
import sys
import hashlib
from time import time, localtime, strftime
from difflib import SequenceMatcher
from typing import Union
import re


class VersionControl():
    """
        A class to track changes within the folder.
    """

    def __init__(self, to_ignore: str = '.vcignore'):
        self.content = []
        # key is a version, value is a list with changes
        self.ignore = self.__vc_ignore(to_ignore)
        self.to_commit = {}

    def init(self):
        """ initiates a version controll system in a cwd """
        self.content = self.ls()  # get all the files in the given folder
        try:
            os.mkdir('commits')
        except:
            print('The commit folder already exists')

        if os.listdir('./commits'):
            # if anything has been committed already
            print('This folder is already being tracked.')
        else:
            for f in self.content:
                if f not in self.ignore:
                    # skip unnecessary files
                    self.add(f)

            self.commit('Initial commit')  # commit updates
            print('This folder is now being tracked for changes')

    def commit(self, message: str):
        # save changes and move a version upwards
        if not message:
            message = input("provide the message for this commit")

        if self.to_commit:
            idx, when, message = self.__hash_commit(message)

            outf = open('./commits/.log', 'a')
            print("%s\t%s\t%s" % (idx, message, when), file=outf)
            outf.close()

            outf = open('commits/%s' % (idx), 'w+')
            print('%s\n' % (when), file=outf)

            for f, changes in self.to_commit.items():
                changes = '<sep>'.join('<sep>'.join(changes).split('\n'))
                print('%s\t%s' % (f, changes), file=outf)
            outf.close()

            self.to_commit = {}
        else:
            print('nothing to commit, add files first')

    def __vc_ignore(self, path: str = '.vcignore'):
        """ update files that have to be excluded from """
        return [f.strip() for f in open(path).readlines()]

    def __hash_commit(self, message: str):
        """ return the details of the commit: id, date and message """
        when = time()
        # use file content and a timestamp to get a unique id
        idx = hashlib.sha256(bytes(message + str(when), 'utf-8')).hexdigest()
        return idx, strftime('%d.%m.%Y %H:%M:%S', localtime(when)), message

    def add(self, fname: str):
        """ add a file to commit """
        try:
            last_commit_id = self.last_commit_id(fname)
        except:
            last_commit_id = False

        if not last_commit_id:
            old = []
        else:
            old = self.restore(fname, last_commit_id).split('\n')

        self.to_commit[fname] = diff(old, fname)

    def modifications(self, fname: str, commit_id: str) -> list:
        """ return the updates for a given file providing the commit_id """
        try:
            changes = open('commits/%s' % (commit_id), 'r').readlines()
        except:
            print('Check the commit_id')

        for entry in changes[2:]:
            # skip timestamp and an empty line
            entry = entry.strip().split('\t')
            if entry[0] == fname:
                return entry[1]

    def restore(self, fname, commit=None) -> str:
        """ returns a file content using only the info about modifications """
        if not commit:
            # return the content of the current file
            return open(fname, 'r').read()

        changes = self.modifications(fname, commit)

        # print(re.split(r"\\n", changes))

        output = ""
        for change in changes.split('<sep>'):
            # handle extra slash
            update = change[:3]
            if update == "+++":
                output += change[3:] + "\n"
            elif update == "---":
                output.replace(change[3:] + '\n', "")
            else:
                output += change + '\n'

        return output.strip()

    def last_commit_id(self, fname: str) -> str or None:
        """ get the id of the commit when the files was modified for the last time """
        commits = self.log()[::-1]
        commits = [commit.split('\t')[0] for commit in commits]

        for commit_id in commits:
            with open('commits/%s' % (commit_id), 'r') as f:
                content = f.readlines()

            for entry in content[2:]:
                # skip timestamp and an empty line
                entry = entry.strip().split('\t')
                if entry[0] == fname:
                    return commit_id

        return None

    def status(self):
        """ prints out if there are any files to commit """
        for f in self.to_commit:
            print(f)

    def log(self):
        """ returns all the commits from latest to earliest """
        with open('commits/.log', 'r') as f:
            output = f.readlines()
        return output

    def __repr__(self):
        """
            lists all the commits and their descriptions for the current folder
            commits are sorted from earliest to oldest
        """
        out = ""
        commits = open('commits/.log', 'r').readlines()

        for commit in commits[::-1]:
            out += commit

        return out

    def ls(self, path='.'):
        """ returns all the files in the given folder + (inner files)"""
        paths = []  # paths to files in the folder
        for fname in os.listdir(path):
            if fname in self.ignore:
                # ignore files from .vcignore
                continue
            elif os.path.isdir(fname):
                # get inner files if it is a directory
                paths.extend(self.ls('%s/%s' % (path, fname)))
                continue

            # add a file to the list of files
            paths.append('%s/%s' % (path, fname))

        return paths


def diff(file1: Union[str, list], file2: Union[str, list]) -> list:
    """compares files using SequenceMatcher's get_opcodes()"""

    if isinstance(file1, str):
        file1 = open(file1, 'r').readlines()
        file1 = [f.strip() for f in file1]
    if isinstance(file2, str):
        file2 = open(file2, 'r').readlines()
        file2 = [f.strip() for f in file2]

    diff = []
    for op in SequenceMatcher(None, file1, file2).get_opcodes():
        if op[0] == 'replace':
            diff.append("\n".join(["---" + line for line in file1[op[1]:op[2]]
                                   ] + ["+++" + line for line in file2[op[3]:op[4]]]))
        elif op[0] == 'delete':
            diff.append(
                "\n".join(["---" + line for line in file1[op[1]:op[2]]])
            )
        elif op[0] == 'equal':
            diff.append(
                "\n".join(["" + line for line in file1[op[1]:op[2]]]))
        elif op[0] == 'insert':
            diff.append(
                "\n".join(["+++" + line for line in file2[op[3]:op[4]]]))

    # remove unnecessary linebreaks before returning
    return [el.strip() for el in diff]
