## Linked lists

### Exercise: use diagrams to explain how to delete an item from a linked list.

 
| x[0] | next | --->-- | x[1] | next | --->-- | x[2] | NULL |
 


 
| x[0] | next | --->-- | x[2] | NULL |
 
              \        /
              ---------------
               | x[1] | next |
              ---------------


 
| x[0] | next | --->-- | x[2] | NULL |
 

            ---------------
             | x[1] | next |
            ---------------



## Trees

### Exercise: assemble the numbers 1-10 into binary search trees which are

1. maximally unbalanced to the left

                        10
                       /
                      9
                     /
                    8
                   /
                  7
                 /
                6
               /
              5
             /
            4
           /
          3
         /
        2
       /
      1

2. balanced

             5
          /     \
        3        7
      /   \    /    \
     2     4  6      9
    /               / \
    1              8   10

3. one step from balanced
             4
          /     \
        2         6
      /   \      /  \
     1     3    5    8
                    / \
                   7   9
                        \
                         10


## Graphs

### Exercise: assemble a directed acyclic graph with the numbers 1-12 by strict divisibility: an edge from A to B if B/A is prime. There are no directed cycles, but some nodes do have multiple paths to them. (These form cycles if you ignore the direction.) Which ones? Explain how to decide if a number will have multiple paths to it.


                  7    5 ->- 10       8
                   ↖  ↗     ↗       ↗
             11 -<-  1  ->- 2  ->- 4
                      ↘      ↘      ↘
                  9 -<- 3 ->- 6 ->-  12


6, 10, 12 - Multiple paths due to the fact that they are devisable by two prime numbers


### Exercise: Identify several maximal spanning trees in the divisibility graph from the previous exercise.

1 -> 2 -> 4 -> 8

1 -> 2 -> 4 -> 12

1 -> 3 -> 6 -> 12

### Exercise: model acquaintance using a graph (vertices are people, an edge between A and B means A knows B). Model it with a directed graph. How are these different?

The previous graph allowed only oneway edges, and this one acquaintance assumes
that A and B can know each other, thus cycles are possible.
