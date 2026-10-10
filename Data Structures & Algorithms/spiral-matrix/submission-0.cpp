class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int left = 0, right = matrix[0].size();
        int top = 0, bottom = matrix.size();
        vector<int> res;
        while (left < right && top < bottom){
            for (int i = left; i < right; i++){
                res.push_back(matrix[top][i]);
            }
            top += 1;

            for(int i = top; i < bottom; i++){
                res.push_back(matrix[i][right - 1]);
            }
            right -= 1;
        
            if (!(left < right && top < bottom)) break;

            for (int i = right - 1; i > left - 1; i--){
                res.push_back(matrix[bottom - 1][i]);
            }
            bottom -= 1;

            for (int i = bottom - 1; i > top - 1; i--){
                res.push_back(matrix[i][left]);
            }
            left += 1;
        } 

        return res;

    }
};
