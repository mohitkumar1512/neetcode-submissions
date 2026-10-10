class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<pair<int, int>> indices;
        for (int i = 0; i < matrix.size(); i++){
            for (int j = 0; j < matrix[0].size(); j++){
                if (matrix[i][j] == 0) {
                    indices.push_back({i, j});
                }
            }
        }
        for (auto [r, c] : indices){
            cout << r << " " << c << endl;
            int i = 1;
            bool res = true;
            while (res){
                res = (zeros(matrix, r + i, c) | zeros(matrix, r - i, c) | zeros(matrix, r, c + i) | zeros(matrix, r, c - i));
                i += 1;
            }  
        }
    }

    bool zeros(vector<vector<int>>& matrix, int r, int c){
        cout << r << " " << c << endl;
        
        if (r < matrix.size() && c < matrix[0].size() && r >= 0 && c >= 0){
            matrix[r][c] = 0;
            return true;
        }
        return false;
    }
};
