class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int,int>> q;
        int fresh = 0;

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 2) q.push({i, j}); // all rotten go in
                if (grid[i][j] == 1) fresh++;         // count fresh
            }
        }
        
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        int minutes = 0;

        while (!q.empty() && fresh != 0){
            int size = q.size();
            minutes += 1;
            for (int i = 0; i < size; i++){
                auto [r, c] = q.front(); q.pop();
                for (auto d : dirs){
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nc >= 0 && 
                        nr < grid.size() && 
                        nc < grid[0].size() &&
                        grid[nr][nc] == 1) {
                            grid[nr][nc] = 2;
                            fresh -= 1;
                            q.push({nr, nc});
                        }

                }
                
            }
        
        }
        return fresh == 0 ? minutes : -1;

    }
};
