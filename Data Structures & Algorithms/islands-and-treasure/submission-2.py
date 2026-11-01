class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi level BFS

        q = deque()
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1,0), (1,0), (0, -1), (0, 1)]
        INF = 2 ** 31 - 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                
        while q:
            r, c = q.popleft()
            for dr, dc in dirs: 
                nr, nc = dr + r, dc + c
                if rows > nr >= 0 and cols > nc >= 0 and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
