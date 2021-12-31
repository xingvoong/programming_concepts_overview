"""
Given an array nums of distinct integers, return all possible permutations.
You can return the answer in any order

Example 1
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 3
Input: nums = [1]
Output: [[1]]

# constraint: they are all unique
"""


def permute(nums):

    n = len(nums)
    result = []

    def backtracking(start, combo):

        if len(combo) == n:
            result.append(list(combo))
            return

        for i in range(start, n):
            # place candidate
            if nums[i] not in combo:
                combo.append(nums[i])
            else:
                continue

            # backtracking
            # if start != i:
            #   continue
            backtracking(start, combo)

            # remove
            combo.pop()

    backtracking(0, [])
    return result


print(permute([1, 2, 3]))
print(permute([1]))
print(permute([0, 1]))

"""
time: O(NxN!)
- copy over: O(N)
- check whether something is in a list: O(N)
- number of permutation: O(N!)
=> total O(NxN!)

space: O(N!)

"""
