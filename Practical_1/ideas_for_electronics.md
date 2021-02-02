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

X | Y | X XOR Y
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
0 | 1 |   0  |     0   |    0   |       0      |    1  |        1           |
1 | 1 |   0  |     0   |    1   |       1      |    1  |        1           |
