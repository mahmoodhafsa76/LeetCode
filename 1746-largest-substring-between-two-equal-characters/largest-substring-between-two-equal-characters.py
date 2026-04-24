class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        n = len(s)
        for i in range(n-1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    res = max(res, j - i - 1)
        return res
