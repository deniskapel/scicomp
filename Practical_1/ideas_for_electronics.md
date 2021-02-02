## Interlude: review of logic

### Exercise: Compute the truth table for NOT:

X | NOT X
--|-------
0 |   1
1 |   0

### Exercise: Compute the truth table table for AND.

X | Y | X AND Y
--|---|--------
0 | 0 |   0
1 | 0 |   0
0 | 1 |   0
1 | 1 |   1

### Exercise: Compute the truth table for exclusive-or, defined by the formula:

XOR(X, Y) = (X OR Y) AND NOT (X AND Y)

X | Y | XOR(X, Y)
--|---|--------
0 | 0 |   0
1 | 0 |   1
0 | 1 |   1
1 | 1 |   0

### Exercise: Prove De Morgan's theorem, NOT(X OR Y) = NOT(X) AND NOT(Y),
by completing the table and checking the last two columns are the same.

X | Y | NOT(X OR Y) | NOT(X) AND NOT(Y)
--|---|-------------|-------------------
0 | 0 |      1      |        1
1 | 0 |      0      |        0
0 | 1 |      0      |        0
1 | 1 |      0      |        0


### Exercise: using truth tables, check these three equations

X | Y |NOT(X)|NAND(1,X)|AND(X,Y)|NOT(NAND(X,Y))|OR(X,Y)|NAND(NOT(X),NOT(Y)))|
--|---|------|---------|--------|--------------|-------|--------------------|
0 | 0 |   1  |     1   |    0   |       0      |    0  |        0           |
1 | 0 |   0  |     0   |    0   |       0      |    1  |        1           |
0 | 1 |   1  |     1   |    0   |       0      |    1  |        1           |
1 | 1 |   0  |     0   |    1   |       1      |    1  |        1           |

### Exercise: write similar formulas expressing NOT, AND, and OR in terms of NOR

* NOT(X) = NOR(0,X)
* AND(X,Y) = NOR(NOT(X),NOT(Y)))
* OR(X,Y) = NOT(NOR(X,Y))

|X | Y | NOT(X) | NOR(0,X) | AND(X,Y) | NOR(NOT(X),NOT(Y))) | OR(X,Y) | NOT(NOR(X,Y)) |
|--- |--- |--- |--- |--- |--- |--- |--- |
|0   | 0  | 1  | 1  | 0  | 0  | 0  |  0 |
|0   | 1  | 1  | 1  | 0  | 0  | 1  | 1  |
|1   | 0  | 0  | 0  | 0  | 0  | 1  | 1  |
|1   | 1  | 0  | 0  | 1  | 1  | 1  | 1  |

### Exercise: why NOT and OR can't be expressed in terms of AND? Explain
In order to use other operators, we first need to define them, so only AND is available to us.
1. NOT in terms of AND is not possible, as it requires different formulas for each of the two values:
* NOT(X) = AND(0, X) only if X == 1
* NOT(X) = AND(1, X) only if X == 0

2. OR in terms of AND is not possible, as it works fine for (0,0) and (1,1) but will fail at (0,1) and (1,0) pairs.
* OR(X,Y) = AND(AND(1,X), AND(1,Y))


## Binary numbers as lists of boolean values

### Exercise: Without listing explicitly, how many possible 8-bit binary numbers are there?
256


### Exercise: Convert X = 110 to decimal.

X2 | X1 | X0
---|----|----
1  | 1  |  0
^    ^     ^--------- times 2^0 = 1
|    |--------------- times 2^1 = 2
|-------------------- times 2^2 = 4

  1 * 2^2 + 1 * 2^1 + 0 * 2^0
= 1 * 4   + 1 * 2   + 0 * 1
=   4     +   2     +   0
= 6

### Exercise: Convert 11 to binary.

high bit is 3 -> X3=1 -> 11-8=3 -> high bit is 1, X1=1, 3-2=1, high bit is 0,
X0=1, thus X = 1011

### Exercise: Convert these powers of 2 into binary: 2, 4, 8, 16, 32. What do you notice?

2 = 10
4 = 100
8 = 1000
16 = 10000
32 = 100000

There is an extra bit with every other power

### Exercise: Convert these numbers into binary: 1, 3, 7, 15, 31 (they are all 2^n - 1 for some n). What do you notice?

1 = 1
3 = 11
7 = 111
15 = 1111
31 = 11111

All these numbers are one bit smaller than their respective powers. By incrementing a decimal by 1, we cause overflow into the next digit.

### Exercise: check that these numbers all have the same 3-bit representation
* 3 = 11 = 17
  - 011 = 1**011** != 10**001**
* 0 = 8 = 16
  - 000 = 1**000** = 10**000**
* 2 = 10 = 18
  - 010 = 1**010** = 10**010**

## Binary arithmetic as logical operations

### Exercise: complete the table by converting 2 into single-bit binary:

X0 | Y0 | Z0
---|----|----
0  | 0  | 0
1  | 0  | 1
0  | 1  | 1
1  | 1  | 0


### Exercise: do the same for single-bit multiplication: write down the table of binary numbers for X0, Y0, and the binary representation of their product Z0, and find the logical operation which matches.

X0 | Y0 | Z0
---|----|----
0  | 0  | 0
1  | 0  | 0
0  | 1  | 0
1  | 1  | 1

AND implements single-bit multiplication

## Digital Logic

### Exercise: Using A and B as the inputs, and OUT as the output, explain how this circuit acts as NAND(A,B); for each entry in the truth table, follow the explanation above. True is "high energy" and False is "low energy".

 A |  B | NAND(A,B) |
---|----|-----------|
0  | 0  | 1         |
1  | 0  | 1         |
0  | 1  | 1         |
1  | 1  | 0         |

If both inputs are low energy, all the energy is spent on crossing the gates. Same happens when either of the gates is unpowered, as the energy is spent on crossing it. Only when both inputs are powered, electrons will travel without losing energy.
