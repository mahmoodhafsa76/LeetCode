class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}
        for p in path:
            dx, dy = self.directional_coordinates(p)
            x += dx
            y += dy
            if (x, y) in visited:
                return True

            visited.add((x, y))
        return False

    def directional_coordinates(self, p):
        if p == "N":
            dir_coordinates = (0,1)

        elif p == "S":
            dir_coordinates = (0,-1)

        elif p == "E":
            dir_coordinates = (1,0)

        else:
            dir_coordinates = (-1,0)
        
        return dir_coordinates

        