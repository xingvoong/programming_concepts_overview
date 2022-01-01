'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order

Example 1:
Input: nums = [1, 1, 2]
Output:
[[1, 1, 2],
 [1, 2, 1],
 [2, 1, 1]
]

- need to have the same counts and frequency

'''

def permute(nums):
  n = len(nums)
  result = []
  count_hashmap = {}
  for i in nums:
    if i in count_hashmap:
      count_hashmap[i] += 1
    else:
      count_hashmap[i] = 1

  def backtracking(combo, count_hashmap):
    # if solutions:
    # output(solution)
    if len(combo) == n:
      result.append(list(combo))
      return
    # visit all the next candidates
    # in this case, the next candidates are frequency count as well
    # only append a key if the count is greater than 0
    # after that, I have to place the count back
    # or revert the choice back for the next explore
    for key in count_hashmap.keys():

      # condition to place a key
      if count_hashmap[key] > 0:
        combo.append(key)
        count_hashmap[key] -= 1

        # backtrack
        backtracking(combo, count_hashmap)

        # revert the choice back for the next explore
        combo.pop()
        count_hashmap[key] += 1

  backtracking([], count_hashmap)
  return result

print(permute([1, 1, 2]))
'''
- the count need to stay the same
- I do not append a number itself
- I have to append the rest of it.

time:
- N! for number of permutation
- N to do deep copy of a list
=> O(N x N!)

space:
 - O(N) at least: for the hashmap
- O(N) for recursive stack on each node, we call backtrack on N nodes.
- O(N) for a copy of a permutation list
total: O(3N) or O(N)
'''