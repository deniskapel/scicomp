# Unix™ for Poets

This is the description of the practicle on Interfaces

## Preparation stage

These three commands are necessary to download files for the practicle

```bash
    wget -c https://dumps.wikimedia.org/enwiki/20210220/enwiki-20210220-pages-articles15.xml-p17324603p17460152.bz2
    wget https://dumps.wikimedia.org/enwiki/20210220/enwiki-20210220-pages-articles15.xml-p17324603p17460152.bz2
    python WikiExtractor.py --infn enwiki*.bz2
```

## Counting

The language of the input file is English, so we are to modify the original bash command

```bash
    sed 's/[^а-яА-ЯIӀ]\+/\n/g' < wiki.txt | sort -r | uniq -c > wiki.hist
```

The output is save into wiki.hist file. This is a sample of it:

```
    16 Guthrie
    2 Guthmann
    1 Guterres
    2 Gutenfels
    5 Gutenberg
```

## More counting

Further modifications of the pipeline:


```bash
    uconv -x upper < wiki.txt | sed 's/[^A-Za-zI]\+/\n/g' | sort -r | uniq -c | sed 5q
```

Comman `sed 5q` limits the output.

```bash
    uconv -x upper < wiki.txt | sed 's/[^AEIOUY]\+/\n/g' | sort -r | uniq -c | sed 5q
```

The output allows to calculate the number of vowel sequences.
```
    1 YYYYYYYY
      1 YYYYYYY
      1 YYYYYY
     19 YYYY
      3 YYY
```

And the same idea with consonants:

```bash
    uconv -x upper < wiki.txt | sed 's/[^BCDFGHJKLMNPQRSTVWXZ]\+/\n/g' | sort -r | uniq -c | sed 5q
```
with its shortened output

```
    3 ZZZZ
    2 ZZZ
    1 ZZW
    2 ZZS
    1 ZZR
```

## Sorting

### Sort the words in Wikipedia by frequency

```bash
    sed 's/[^A-Za-zI]\+/\n/g' < wiki.txt | sort | uniq -c | sort -nr
```

The output is creadible as all the words would be in the following form:

```
    223253 the
    117586 of
    106772 
    105109 and
    94137 in
```

### Sort them by folding case.
```bash
    sed 's/[^A-Za-zI]\+/\n/g' < wiki.txt | sort | uniq -c | sort -f
```

Lowercase letters come before uppercase ones: 

```
    1001 D
    10054 He
    100 aerial
    100 Along
    100 Anglican
```

### Sort them by ''rhyming'' order.

```bash
    sed 's/[^A-Za-z]\+/\n/g' < wiki.txt | sort | uniq -c | rev | sort -f | rev
```

It is fantastic. I never thought about an approach to find rhyming words so efficiently:

```
    3 pointy
    7 Monty
    2 Ponty
    2 Aunty
    1 jaunty
    1 Bounty
    3 bounty
```

## Bigrams + Shell scripts

```bash
    sed 's/[^A-Za-z]\+/\n/g' | grep -v '^$' > $$words
    tail -n +2 $$words > $$nextwords
    paste $$words $$nextwords |
    sort | uniq -c | sort -nr
    # remove the temporary files
    rm $$words $$nextwords
```

Like a charm (though it might be good to remove space-to-space and space-to-token examples):

```
    35705 of	the
    25094 in	the
    12490 to	the
```

##  grep: An Example of a Filter

```bash
    grep 'Rhode Island' wiki.txt | sh bigram.sh | sort -nr | sed 5q
```

Testing on a meaningful bigram rather than on prepositions and articles: 

```
    949 Rhode   Island
    647 of      the
    472 is      a
    440 in      the
    288 to      the
```

Excluding all pairs with short tokens

```bash
    grep -E '[a-z]{,3} [a-z]{,3}' -i --invert-match wiki.txt | sh bigram.sh | sort -nr | sed 5q
```

```
    171 onlyinclude     onlyinclude
    101 History History
    46 History Description
    43 Career  History
    42 Plot    Production
```

## Exersices with grep


### How many uppercase words are there in the text? Lowercase? Hint: wc -l or grep -c

Uppercase: NYU    

```bash
    sed 's/[^A-Za-z]\+/\n/g' < wiki.txt   | grep -E '^[A-Z]{2,}$' -c
```

33961 tokens 

Lowercase: descendants

```bash
    sed 's/[^A-Za-z]\+/\n/g' < wiki.txt   | grep -E '^[a-z]{2,}$' -c 
```

2517934 tokens

### How many 4-letter words?

```bash
    sed 's/[^A-Za-z]\+/\n/g' < wiki.txt | grep -E '^[a-z]{4}$' -i -c 
```

444655 tokens

### Are there any words with no vowels?

```bash
    sed 's/[^A-Za-z]\+/\n/g' < wiki.txt | grep -E '^[^aeiouy]{2,}$' | sed 15q 
```

Yes, there are, e.g. SFL, SPFL, MTV, Mr, Ms


### Find ''1-syllable'' words (words with exactly one vowel)
```bash
    sed 's/[^A-Za-z]\+/\n/g' < wiki.txt | grep -E '^[^aeiouy]*[aeiouy][^aeiouy]*$' -i | sed 5q 
```

These are The, first, batch, of, VE, did, not and many others.


### Find ''2-syllable'' words (words with exactly two vowels)
```bash
    sed 's/[^A-Za-z]\+/\n/g' < wiki.txt | grep -E '^[^aeiouy]*[aeiouy]{1,2}[^aeiouy]*[aeiouy]{1,2}[^aeiouy]*$' -i | sed 5q 
```


These are league, number, were, play, football, either and many others.


## Exercises with sed

### Count word initial consonant sequences: tokenise by word, delete the vowel and the rest of the word, and count

To remove diacritics as well.

```bash
    sed 's/[^A-Za-z]\+/\n/g' < wiki.txt |
    sed 's/\([^BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz].\{0,\}\)//g' | awk 'NF' |   
    sort -r | uniq -c | sort -nr | sed 5q
```

awk 'NF' removes empty sequence

```
    284495 th
    125761 w
    120049 s
    118108 t
    106815 b
```

### Count word final consonant sequences

Reversing twice let us reuse the regex

```bash
    sed 's/[^A-Za-z]\+/\n/g' < wiki.txt | rev |
    sed 's/\([^BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz].\{0,\}\)//g' | awk 'NF' | rev |   
    sort -r | uniq -c | sort -nr | sed 5q
```

```
    352109 n
    289020 s
    211489 r
    193796 d
    135700 nd
    121969 f
    114012 t
```