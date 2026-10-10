class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
    // step 1: transpose
    for (int r = 0; r < n; r++)
        for (int c = r + 1; c < m; c++)  // c starts at r+1 to avoid double swap
            swap(matrix[r][c], matrix[c][r]);

    // step 2: reverse each row
    for (int r = 0; r < n; r++)
        reverse(matrix[r].begin(), matrix[r].end());
    }
};
