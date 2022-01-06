"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

- Only numbers 1 through 9 are used
- Each number is used at most once =

Return a list of all possible valid combinations.  The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:

Input: k = 3, n = 7
Output: [[1, 2, 4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations

Example 2:
Input: k = 3, n = 9
Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation:  There are no valid combinations
Using 4 diffrent nu,bers in the range [1, 9], the smallest sum we can get is 1 + 2 + 3 + 4 = 10 and since 10 > 1, there are no valid combination

"""


def combination(k, n):
    result = []

    def backtracking(remain_sum, current, combo):
        if remain_sum == 0 and len(combo) == k:
            # make a deep copy
            result.append(list(combo))
            return
        elif remain_sum < 0:
            return
        else:
            # visit all the next candidates
            for _next in range(current, 10):
                # place the next candidate
                combo.append(_next)

                # backtracking
                backtracking(remain_sum - _next, _next + 1, combo)

                # remove the next candidates
                combo.pop()

    backtracking(n, 1, [])

    return result


print(combination(3, 7))
print(combination(3, 9))
print(combination(4, 1))
print(combination(2, 18))

"""
time:
- the most combination:
if 3 digit: 9*8*7
N! / (N-k)!
- for each combination, we need to make a deep copy
- a deep copy with the longest length is k


space:

grow at most k height
O(k)

"""
