class Solution {
public:
    int perimeter = 0;
    int islandPerimeter(vector<vector<int>>& grid) {
        int perimeter = 0;
        int m = grid.size(), n = grid[0].size();
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    for (auto& d : dirs) {
                        int r = i + d[0], c = j + d[1];
                        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0)
                            perimeter += 1;
                    }
                }
            }
        }
        return perimeter;
    }
};