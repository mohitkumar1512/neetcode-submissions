class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        queue<pair<int,int>> q;

        // Step 1: seed queue with all treasures
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 0)
                    q.push({i, j});

        // Step 2: BFS outward
        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        while (!q.empty()) {
            auto [r, c] = q.front(); q.pop();

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                // only visit unvisited land cells (INF)
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                if (grid[nr][nc] != INT_MAX) continue; // wall or already visited

                grid[nr][nc] = grid[r][c] + 1; // distance from treasure
                q.push({nr, nc});
            }
        }
    }
};