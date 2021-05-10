## Exercise: using the difflib.SequenceMatcher class, implement a unified diff program in Python. (Note: difflib has many other classes, some of which implement the solution for you! I want you to use SequenceMatcher only, and not rely on the other classes.)

The solution is stored in [diff.py](diff.py) file.

```python3
    $ python3 diff.py old.txt new.txt 
    ---aaa
    bbb
    ccc
    ddd
    +++111
    eee
    ---fff
    +++ggg
```

### Exercise: Implement a simple version control system then would store at each stage a diff from the previous stage. You can make calls to diff and patch if you like.

Using the diff function and a class [VersionControl](utils.py), it tracks changes by creating a commit file for each desired modification. Run `make` before starting the folder to restore the files and delete `commits` folder

```python3
    $ python3 version_control.py 
    This folder is now being tracked for changes

    ddca58d56fccf6820c69a1243065dbc372d5d1a6178026d8aa40313de878f865	Update new.txt file	10.05.2021 12:35:39
    90421a06dd71cfeff032f501367a00d6d01dc01972d75a733b9423405f6d495b	Update new.txt file	10.05.2021 12:35:37
    19c2c49eede0f86708d02a3b7cb74e36aac84aea2fbbe886882b7b164d67685c	Initial commit	10.05.2021 12:35:35

```

### Exercise: How would you handle non-text documents? Suppose you are writing music, drawing a painting, mixing and resampling music. How can you track changes to this? Give an explanation, but no code is expected.

All these types of documents consist of bytes. By comparing bystrings, it is possible to track the difference

### Exercise: Change your version control system to store previous-commit-id with the diff as described above.

The [utils.py](utils.py) file contains a class called `VersionControl`. This class uses the hash_commit() method to create a unique info about each commit. Each commit is than added to the [.log](commits/.log) file to store all the commits in the ascending order. Updates are stored in [commits](commits/) folder named after their commit's ids.  

### Exercise: Write export and import commands which print and read a sequence of commits (where commit = prev commit id + patch). The sequence is called a "changeset."

`VersionControl.__repr__()` prints out the log of changes from earliest to oldest. The `vc.log()` function does the same but in the initial order. Using this information, it is possible to extract a version of a file using the filename and a commit_id