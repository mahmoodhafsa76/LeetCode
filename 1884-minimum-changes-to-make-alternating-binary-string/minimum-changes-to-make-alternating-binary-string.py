class Solution:
    def minOperations(self, s: str) -> int:
        alter_str1, alter_str2 = self.alternatingStringGenerator(s)
        count1, count2 = 0, 0
        for i in range(len(s)):
            if int(s[i]) ^ int(alter_str1[i]):
                count1 += 1

        for i in range(len(s)):
            if int(s[i]) ^ int(alter_str2[i]):
                count2 += 1
        return min(count1, count2)

    def alternatingStringGenerator(self, s):
        n = len(s)
        str1 = ('01' * (n//2)) + ( '0' if n % 2 else '')
        str2 = ('10' * (n//2)) + ( '1' if n % 2 else '')
        return str1, str2
        