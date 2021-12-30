'''
Given an integer array nums of unique elements, return all possible subsets (the power set).  The solution set must not contain duplicates subsets.  return the solution in any order

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

I: a list of numbers
O: a list of lists
C: no duplicate, all unique
E: no empty list

For this approach, I do not need to check for the stopping condition
because all the combo would work, and the for loop will check for the size
of the final result

'''

def subsets(nums):
  result = []
  n = len(nums)

  def backtracking(combo, start):
    # if find solution:
      # output(solution)
      # return
    # in this case, all the nodes are solution
    result.append(list(combo))
    # visit all the next candidates
    for i in range(start, n):
      # place a candidate
      combo.append(nums[i])
      # backtracking
      backtracking(combo, i+1)
      # remove a candidate
      combo.pop()
  # call backtracking
  backtracking([], 0)
  return result

input1 = [1, 2, 3]
input2 = [0]

print(subsets(input1))

'''
time: O(2^N) for creating the subset 2^N
space: O(N) the max heigh of the tree

'''