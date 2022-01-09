"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))", "(()())","(())()", "()(())", "()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Contraints:
- 1 <= n <= 8

# only append when opening < n
# only append the closing parenthesis when closing < opening
"""


def generateParenthesis(n):
    result = []

    def backtracking(combo, left, right):
        if len(combo) == 2 * n:
            result.append("".join(combo))
            return
        # visit all the next candidates
        if left < n:
            # place a candidate
            combo.append("(")
            # backtracking
            backtracking(combo, left + 1, right)

            # remove a candidate
            combo.pop()

        if right < left:
            # place a candidate
            combo.append(")")
            # backtracking
            backtracking(combo, left, right + 1)

            # remove a candidate
            combo.pop()

    backtracking([], 0, 0)

    return result


print(generateParenthesis(3))
