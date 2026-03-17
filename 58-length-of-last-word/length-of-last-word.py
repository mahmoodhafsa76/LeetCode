class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr_str = s.split()
        str_len = len(arr_str[-1])
        return str_len
        