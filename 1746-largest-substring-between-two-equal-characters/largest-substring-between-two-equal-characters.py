class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        index1 = {}
       
        for i, c in enumerate(s):
            if c in index1:
                res = max(res, i - index1[c] - 1)
            else:
                index1[c] = i
            
            

        return res