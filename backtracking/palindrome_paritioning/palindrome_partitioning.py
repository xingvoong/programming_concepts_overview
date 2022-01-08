"""
Given a string s, partition as such that every substring of the partition is a palindrome.  Return all possible palindrome paritioning of s.

A palindrome string is a string that reads the same backward as forward

Example 1:
Input: s = "aab"
Output: [["a", "a", "b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters.

- generate all the possbile strings and check whether a string is palindrome
+ if a string is not palindrom then I do not go down that round (prune the work)
"""


def isPalindrome(start, end, s):
    while start <= end:
        print("hello")
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True


def partition(s):
    """

    :type s: str
    :rtype: List[List[str]]

    """

    def isPalindrome(start, end, s):
        while start <= end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

    def backtracking(start, combo):
        # that means we exhaust all the possible letters

        if start >= n:
            result.append(list(combo))
            return

        # visit all the next candidates
        for _next in range(start, n):
            # place a candidate
            if isPalindrome(start, _next, s):
                combo.append(s[start : _next + 1])

                backtracking(_next + 1, combo)
                combo.pop()

    n = len(s)
    result = []
    backtracking(0, [])
    return result


# print(isPalindrome(0, 3, "aabc"))

print(partition("abbab"))

"""
time: O(N x 2^N)
space: O(N)

"""
