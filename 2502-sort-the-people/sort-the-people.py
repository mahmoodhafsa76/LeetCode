class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_names = {}
        for h, n in zip(heights, names):
            heights_names[h] = n

        res = []
        for h in reversed(sorted(heights_names)): 
            res.append(heights_names[h])        

        return res
        