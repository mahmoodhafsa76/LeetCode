class Solution:
    def longestPalindrome(self, s: str) -> int:
        mask1 = 0  # [a - z]
        mask2 = 0  # [A - Z]
        res = 0

        for c in s:
            if 'a' <= c <= 'z':
                bit = 1 << (ord(c) - ord('a')) # assigns value to the character position
                if mask1 & bit: # checks if the bit at the character position is even or odd (0 or 1)
                    res += 2
                mask1 ^= bit  # toggles character bit position after each pass 
            else:
                bit = 1 << (ord(c) - ord('A'))
                if mask2 & bit:
                    res += 2
                mask2 ^= bit

        return res + 1 if mask1 or mask2 else res
        
