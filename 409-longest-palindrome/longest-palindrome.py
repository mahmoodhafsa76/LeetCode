class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = set()
        result = 0

        for char in s:
            if char in count:
                count -= {char}
                result += 2

            else:
                count.add(char)
        
        if count:
            result += 1

        return result

        
