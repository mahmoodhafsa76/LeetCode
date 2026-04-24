class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        index1 = {}
        index2 = {}

        for i, c in enumerate(s):
            if c in index1:
                index2[c] = i
            else:
                index1[c] = i

        for c in index2:
            res = max(res, index2[c] - index1[c] - 1)

        return res