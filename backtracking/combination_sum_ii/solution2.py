'''
Given a collection of candidates numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidates numbers sum to target

Each number in candidates may only be used once in the combination (Do not go back for the previous number)
or count the frequency

Note:  the solution set must not contain duplicate combinations (how do I avoid this?)

Example 1:
Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
Output:

[
  [1, 1, 6],
  [1, 2, 5],
  [1, 7],
  [2, 6]
]

Example 2:
Input: candidates = [2, 5, 2, 1, 2], target = 5
Output:
[
  [1, 2, 2],
  [5]
]

Constraints:
- 1 <= candidates.length <= 100
- 1 <= candodates[i] <= 50
- 1 <= target <= 30

'''
def combinationSum2(candidates, target):
  n = len(candidates)
  result = []
  # candidates.sort
  candidates.sort()
  # print(candidates)

  def backtracking(remain_sum, current, combo):
    if remain_sum == 0:
      result.append(list(combo))
      return
    elif remain_sum < 0:
      return
    else:
      # visit all the next candidates
      for next_candidate in range(current, n):
        if candidates[next_candidate] == candidates[next_candidate-1] and next_candidate > current:
          continue
        combo.append(candidates[next_candidate])
        backtracking(remain_sum - candidates[next_candidate], next_candidate + 1, combo)
        combo.pop()

  backtracking(target, 0, [])
  return result

print(combinationSum2([10,1,2,7,6,1,5], 8))
# print(combinationSum2([2, 5, 2, 1, 2], 5))

'''
time: O(N* 2^N)

space: O(N)
'''





