class Solution {
public:
    set<pair<int,int>> visited;
    int rows = -1;
    int cols = -1;

    bool exist(vector<vector<char>>& board, string word) {
        rows = board.size();
        cols = board[0].size();
        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                if (dfs(board, word, 0, r, c)) return true;
            }
        }
        return false;
    }
    bool dfs(vector<vector<char>>& board, string word, int index, int r, int c) {
        if (index >= word.size()) return true;
        if (r < 0 || r >= rows || c < 0 || c >= cols) return false;
        if (visited.count({r, c}) || board[r][c] != word[index]) return false; 

        visited.insert({r, c});
        bool res = (
            dfs(board, word, index + 1, r - 1, c) || 
            dfs(board, word, index + 1, r + 1, c) ||
            dfs(board, word, index + 1, r, c - 1) ||
            dfs(board, word, index + 1, r, c + 1)
        );
        visited.erase({r, c});
        return res;
    }   
};
