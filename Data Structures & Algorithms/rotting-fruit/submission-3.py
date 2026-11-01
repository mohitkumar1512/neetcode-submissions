class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source BFS 
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_oranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh_oranges += 1
        minutes = 0
        while q and fresh_oranges > 0: 
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if  0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: 
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh_oranges -= 1
                
        
        return minutes if fresh_oranges == 0 else -1 

