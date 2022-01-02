'''
Given an array of distinct integers candidates and a tagret integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.  You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.  Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum to target is less tha 150 combinations for the given input.

I: a list of num and a target
O: a list of lists
C:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct
1 <= target <= 50
E:
'''

def combinations(candidates, target):

  n =  len(candidates)
  result = []
  # if solutions:
  # output(solution)
  def backtracking(remain_sum, combo, start):
    if remain_sum == 0:
      result.append(list(combo))
      return
    # if less than 0: mean the sum of nodes are currently too big
    elif remain_sum < 0:
      return
    else:
      # visit all the next candidates:
      for i in range(start, n):

        # place the next candidate:
        combo.append(candidates[i])

        # backtracking:
        backtracking(remain_sum - candidates[i], combo, i)

        # revert the previous choice for other exploration
        combo.pop()


  backtracking(target, [], 0)

  return result

input1 = [2, 3, 6, 7]
target1 = 7

input2 = [2, 3, 5]
target2 = 8

input3 = [2]
target3 = 1

print(combinations(input1, target1))
print(combinations(input2, target2))
print(combinations(input3, target3))


'''
let N be the number of candidates
T is the target value
M is mininum value

time: O(N^T/M)


- O(N) to deep copy a list
- 2^N the number of possible nodes
space: O(N)
- log2(N^2), the maxinum height of the tree => wrong

space: O(T/M)

- we implement the algorithms in recursion, which consumes some additional memory in the functuon call stack
- the number of recursive calls can pile up to T/M, where we keep on adding the smallest element to the combination.  As a result, the space overhead of the recursion is O(T/M)
=> The height of the tree

- In addition, we keep a combination of numbers during the execution, which requires at most O(T/M) space as well.
- To sum up, the total space complexity of the algorithm would be O(T/M)
- Note that, we did not take into the account the space used to hold the final results for the space complexity

=> How deep a tree can be, or what is the height of the tree.
So I can know the space, and the power of the work
'''

