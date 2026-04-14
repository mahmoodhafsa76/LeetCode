class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for i in range(len(paths)):
            for j in range(2):
                s.add(paths[i][0])


        for i in range(len(paths)):
            for j in range((2)):
                if paths[i][1] not in s:
                    return paths[i][1]



        