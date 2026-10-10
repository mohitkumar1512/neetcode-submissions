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
            // int i = 1;
            // bool res = true;
            // while (res){
            //     res = (zeros(matrix, r + i, c) | zeros(matrix, r - i, c) | zeros(matrix, r, c + i) | zeros(matrix, r, c - i));
            //     i += 1;
            // } 
             
            for (int j = 0; j < matrix[0].size(); j++)
                matrix[r][j] = 0;
            for (int i = 0; i < matrix.size(); i++)
                matrix[i][c] = 0;
        }
    }

    // bool zeros(vector<vector<int>>& matrix, int r, int c){
        
    //     if (r < matrix.size() && c < matrix[0].size() && r >= 0 && c >= 0){
    //         matrix[r][c] = 0;
    //         return true;
    //     }
    //     return false;
    // }
};
