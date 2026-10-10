class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited_p = set()
        visited_a = set()
        rows = len(heights)
        cols = len(heights[0])
        def dfs(r, c, visited, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < prev:
                return 

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for r in range(rows): 
            for c in range(cols): 
                # pacific
                if c == 0 or r == 0:
                    dfs(r, c, visited_p, 0)

                #atlantic
                if c == cols - 1 or r == rows - 1:
                    dfs(r, c, visited_a, 0)
        
        res = []
        for p in visited_p:
            if p in visited_a:
                res.append(list(p))
        
        return res

