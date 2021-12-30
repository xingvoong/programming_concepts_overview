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

combo is the current subset
start is the start of number in nums input
size: the size of the subset
- I start at size 1, and increase the size each time

'''

def subsets(nums):
  result = []
  n = len(nums)
  def backtracking(combo, start, size):
    if len(combo) == size:
      result.append(list(combo))
      return
    else:
      for i in range(start, n):
        combo.append(nums[i])
        backtracking(combo, i+1, size)
        combo.pop()

  for i in range(n+1):
    backtracking([], 0, i)

  return result

input1 = [1, 2, 3]
input2 = [0]

print(subsets(input1))