"""
Given two integers n and k, return all possible combnations of k numbers out of the range [1, n]

You may return the answer in any order

Example 1:

input: n = 4, k = 2
output:
[
  [2, 4],
  [3, 4],
  [2, 3],
  [1, 2],
  [1, 3],
  [1, 4]
]


candidates = [1, 2, 3, 4]
1: No duplicate
2: I do not need to revisit one of the previous node


example 2:
input: n = 1, k = 1
output: [[1]]


the size of k have to decrease:
=> remain k
combo: which is the current combination
start: where we are in the range of n
"""


def combine(n, k):
    result = []

    def backtracking(combo, start):
        if len(combo) == k:
            result.append(list(combo))
            return
        else:
            # visit all the next candidates
            for i in range(start, n + 1):
                # place the next candidate
                combo.append(i)
                # backtracking
                backtracking(combo, i)
                # remove the next candidate
                combo.pop()

    backtracking([], 1)
    return result


input1 = 4
k1 = 2

input2 = 1
k2 = 1

print(combine(input2, k2))

"""
right now: k get decrease tho


"""
