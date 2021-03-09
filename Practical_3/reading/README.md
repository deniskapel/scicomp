# Interfaces I

## Command-line and text interfaces

### Exercise: Give two examples of asynchronous communication. Give two examples of synchronous communication.

asynchronous: emails, blogs
synchronous:  phone calls, and video conference

## Using a CLI

### Exercise: Compare the output of ls vs ls -l and ls -a; describe how they are similar, and how they are different.

ls outputs only names of files and repositories in the current repository.

ls -l will show detailed information about the files in the current repository.

ls -a will output all the files including those starting with .

### Exercise: Explain pushd and popd; what data structure represents your directory history? Give an example of using them to organise a folder with music.

These are tools to move between working directories. After adding a folder with pushd, index 0 is assigned to it, other folders are shifted to +1 positions. Command popd will remove the first element of the list. Later, it is possible to navigate between folders using just their index, e.g. cd ~1

```bash
    dirs -v
    0  ~/music/pop/madonna
    1  ~/music/pop/mjackson
    2  ~/music/pop
    3  ~/music/rock
    4  ~/music
```

### Exercise: Draw a partial tree of your filesystem, starting from the children of your home directory. Include ancestors of your home directory, and siblings of those ancestors. Exclude files, just show directories.

    .
    ├── bin
    ├── boot
    ├── dev
    ├── etc
    ├── home
        └── dk
            ├── Desktop
            ├── Documents
            ├── Downloads
            ├── Music
            ├── nltk_data
            ├── Pictures
            ├── Public
            ├── shared-drives
            ├── snap
            ├── Templates
            └── Videos
    ├── lib
    ├── lost+found
    ├── media
    ├── mnt
    ├── opt
    ├── proc
    ├── root
    ├── run
    ├── sbin
    ├── snap
    ├── srv
    ├── sys
    ├── tmp
    ├── usr
    └── var

## Shell scripting

### Exercise: Write a shell script that asks the user for their name, and greets them.

```bash
    #!/bin/bash
    # Proper header for a Bash script.

    while [[ $name = "" ]]
    do
      echo -n "What is your name? "
      read name
    done

    echo "Hello, $name"
    exit 0
```


### Exercise: Write a shell script that performs "ROT13" (Caesar cipher with shift 13.) For English, encryption and decryption are the same! (Explain why!) Sample interaction:

There are 26 characters in English alphabet, so it is devided by 13 into two equal halves. Adding shift to index and

```bash
    #!/bin/bash

    LETTERS=abcdefghijklmnopqrstuvwxyz

    while [[ $msg = "" ]]
    do
      echo -n "Enter a message to encode or decode? "
      read msg
    done

    ouput=""

    for (( i=0; i<${#msg}; i++ )); do
        letter=${msg:$i:1}
        if [[ $LETTERS =~ $letter ]]; then
            shift=$(((12 + `expr index "$LETTERS" $letter`) % 26))
            output+=${letter/$letter/${LETTERS:$shift:1}}
        fi
    done

    echo $output
    exit 0
```

### Exercise: Write a shell function that prints "hidden" if the current directory starts with a dot ".", or if any parent starts with a dot. (Files and directories that start with dots are considered "hidden" on many UNIX-like systems.)

```bash
    #!/bin/bash

    PWD=`pwd`
    PATTERN='/\.'

    if [[ $PWD =~ $PATTERN ]]; then
        echo hidden
        exit 0
    fi

    exit 0
```
