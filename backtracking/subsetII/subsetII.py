"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set)

The solution set must not contain duplicate subsets.  Return the solution in any order.

Input: nums = [1, 2, 2]
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

1: sort it
2: ignore the duplicate in the for loop
3: not outside
"""


def subsetWithDup(nums):

    n = len(nums)
    nums.sort()
    result = []

    def backtracking(start, combo):
        # if solution:
        # then output solution
        # but everynode is a solution so no if needed
        result.append(list(combo))
        # visit all the candidates
        # but do not revisit the old one
        # ignore duplicate in here
        for i in range(start, n):
            # place the next candidate
            if -1 < i < n and nums[i] == nums[i - 1] and i != start:
                continue

            combo.append(nums[i])

            # backtracking
            backtracking(i + 1, combo)

            # remove the next candidate
            combo.pop()

    backtracking(0, [])
    return result


input1 = [0]
input2 = [1, 2, 2, 3]

# print(subsetWithDup([1, 2, 2,]))
print(subsetWithDup(input2))

"""
time: O(N x 2^N)
- 2^n is the number of subsets
- N is the work need to do to copy over a subset


"""
