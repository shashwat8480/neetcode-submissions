class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set() 
        row = len(grid)
        col = len(grid[0])

        def dfs(r,c): 
            if (r < 0 or r == row or c < 0 or c == col or grid[r][c] == 0):
                return 1
            
            if (r,c) in visited: 
                return 0

            visited.add((r,c))

            perim = dfs(r, c+1)
            perim += dfs(r,c-1)
            perim += dfs(r+1,c)
            perim += dfs(r-1,c)

            return perim
        
        for r in range(row): 
            for c in range(col): 
                if grid[r][c] == 1: 
                    return dfs(r,c)
            


