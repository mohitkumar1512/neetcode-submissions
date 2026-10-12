class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        # Brute force:
        #   For every cell in island A, run a separate BFS to find the
        #   nearest cell of island B. Take the min.
        #   O((n^2)^2) since island A can have O(n^2) cells, each BFS O(n^2).

        # Optimized (DFS + multi-source BFS):
        #   1. DFS from the first 1 found -> that's island A. Mark its cells
        #      as 2 (so we can tell A from B) and push them all into the queue.
        #   2. BFS outward from ALL of A at once (like Rotting Oranges).
        #      Each layer = one more water cell flipped.
        #      First time a neighbor is 1 -> that's island B -> return layer count.
        #   Time: O(n^2), each cell visited once
        #   Space: O(n^2), queue + recursion stack

        # Solution:
        N = len(grid)
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()

        # Phase 1: flood island A, mark as 2, collect into queue
        def dfs(r, c):
            if r < 0 or r >= N or c < 0 or c >= N or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r, c))
            for dr, dc in DIRS:
                dfs(r + dr, c + dc)

        def find_first_island():
            for r in range(N):
                for c in range(N):
                    if grid[r][c] == 1:
                        dfs(r, c)
                        return          # stop after ONE island (clean way to exit nested loops)

        find_first_island()
        # Phase 2: grow island A ring by ring until we touch B
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if grid[nr][nc] == 1:       # untouched land = island B
                            return dist
                        if grid[nr][nc] == 0:       # water -> flip it, keep growing
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            dist += 1                               # finished a ring

        return dist