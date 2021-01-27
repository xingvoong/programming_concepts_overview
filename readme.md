An overview of programming concepts such as dynamic programming and backtracking with code.

# Dynamic Programming
source and references:
 1. freeCodeCamp.org https://www.youtube.com/watch?v=oBt53YbR9Kk&t=3027s
 2. CS 170 at UC Berkeley
 https://cs170.org/ 
 
Dynamic Programming problems can be solved using two main techniques:
## 1. Memoization
there are two main steps:
**1. Solve the problem in anyway.**
 - visualize the problem as a tree
 - implement the tree using recursion
 - test the function
**2. Make it efficient**
- add a memo object.  In python, add a dictionary
- add a base case to return memo values
- store memo value in the memo

## 2. Tabulation
- visualize the problem as a table
- size the table based on the inputs
- initialize the table with default values
- seed the trivial answer into the table
- iterate through the table
- fill further positions based on the current position

## 3. Conclusion
- notice any overlapping subproblems
- decide what is the trivially smallest input
- think recursively to use memoization
- think iteratively to use tabulation
- draw a strategy first
 
