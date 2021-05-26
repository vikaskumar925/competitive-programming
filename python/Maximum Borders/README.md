**Problem**
You are given a table with  rows and  columns. Each cell is colored with white or black. Considering the shapes created by black cells, what is the maximum border of these shapes?

A shape is a set of connected cells. Two cells are connected if they share an edge. Note that no shape has a hole in it.

**Input format**

The first line contains  denoting the number of test cases.
The first line of each test case contains integers  denoting the number of rows and columns of the matrix. Here, '#' represents a black cell and '.' represents a white cell. 
Each of the next  lines contains  integers.
**Output format**
Print the maximum border of the shapes.

**Sample Input**
10

2 15

.....####......

.....#.........

7 9

...###...

...###...

..#......

.####....

..#......

...#####.

.........

18 11

.#########.

########...

.........#.

####.......

.....#####.

.....##....

....#####..

.....####..

..###......

......#....

....#####..

...####....

##.........

#####......

....#####..

....##.....

.#######...

.#.........

1 15

.....######....

5 11

..#####....

.#######...

......#....

....#####..

...#####...

8 13

.....######..

......##.....

########.....

...#.........

.............

#######......

..######.....

####.........

7 5

.....

..##.

###..

..##.

.....

..#..

.#...

14 2

..

#.

..

#.

..

#.

..

..

#.

..

..

..

#.

..

7 15

.###########...

##############.

...####........

...##########..

.......#.......

.....#########.

.#######.......

12 6

#####.

###...

#.....

##....

###...

......

.##...

..##..

...#..

..#...

#####.

####..

**Sample Output**
4

5

9

6

5

7

2

1

11

5

