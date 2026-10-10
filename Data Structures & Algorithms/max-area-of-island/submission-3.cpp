class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int numIslands = 0;

        for (int i = 0; i < grid.size(); i++){
            for (int j = 0; j < grid[0].size(); j++){
                if (grid[i][j])
                    numIslands = max(numIslands, dfs(grid, i, j));
            }
        }
        return numIslands;
    }
    int dfs(vector<vector<int>>& grid, int r, int c) {
        if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size()) return 0;
        if (grid[r][c] == 0) return 0;

        grid[r][c] = 0;

        return 1 + dfs(grid, r+1, c)
                + dfs(grid, r-1, c)
                + dfs(grid, r, c+1)
                + dfs(grid, r, c-1);
    }
};
