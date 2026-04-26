class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        index = [-1] * 26
       
        for i in range(len(s)):
            j = ord(s[i]) - ord('a')  # j is the represents indices of index array
            if index[j] != -1:
                res = max(res, i - index[j] - 1)
            else:
                index[j] = i

        return res