class Solution {
public:
    int rows = -1, cols = -1;
    vector<vector<int>> heights;
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& h) {
        set<pair<int, int>> pacific, atlantic;
        heights = h;
        rows = heights.size(); 
        cols = heights[0].size();

        
        vector<vector<int>> res;

        for (int r = 0; r < rows; r++) {
            dfs(r, 0, pacific, heights[r][0]);
            dfs(r, cols-1, atlantic, heights[r][cols-1]);
        }
        for (int c = 0; c < cols; c++) {
            dfs(0, c, pacific, heights[0][c]);
            dfs(rows-1, c, atlantic, heights[rows-1][c]);
        }
       
        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                if (atlantic.count({r, c}) && pacific.count({r, c})){
                    res.push_back({r,c});
                }
            }
        }
        return res;

    }
    void dfs(int r, int c, set<pair<int,int>>& visited, int prevHeight){
        if ( visited.count({r, c}) || 
             r < 0 || c < 0 || r == rows || c == cols ||
             heights[r][c] < prevHeight ) return;

        visited.insert({r, c});
        dfs(r + 1, c, visited, heights[r][c]);
        dfs(r, c + 1, visited, heights[r][c]);
        dfs(r - 1, c, visited, heights[r][c]);
        dfs(r, c - 1, visited, heights[r][c]); 
    
    }
};
