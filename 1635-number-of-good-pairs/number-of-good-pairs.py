class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for num, c in count.items():

            # // is used to keep everything as int.
            #  In c * (c-1), one of c or c-1 is always even (they are consecutive integers, so onemust        #    be even). That means the product is always divisible by 2 with no remainder.
            res += c * (c - 1) // 2

            # the above formula is the simplified version of nCr 


        return res