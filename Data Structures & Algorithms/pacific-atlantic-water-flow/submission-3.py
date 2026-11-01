class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited_pacific, visited_atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def dfs(r, c, visited, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < prev:
                return 

            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                dfs(nr, nc, visited, heights[r][c])
            
        for r in range(rows): 
            for c in range(cols): 
                # pacific
                if c == 0 or r == 0:
                    dfs(r, c, visited_pacific, 0)

                #atlantic
                if c == cols - 1 or r == rows - 1:
                    dfs(r, c, visited_atlantic, 0)
        
        res = []
        for p in visited_pacific:
            if p in visited_atlantic:
                res.append(list(p))
        
        return res