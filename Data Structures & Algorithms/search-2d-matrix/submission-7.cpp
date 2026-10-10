class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = 0;

        int l = 0, r = matrix.size() - 1;

        while (l <= r){
            int mid = l + (r - l) / 2;
            if (matrix[mid][0] <= target && matrix[mid][matrix[mid].size() - 1] >= target){
                row = mid;
                break;
            }
            else if (matrix[mid][0] < target){
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        l = 0, r = matrix[row].size() - 1;
        while (l <= r){
            int mid = l + (r - l) /2;
            if (matrix[row][mid] == target){
                return true;
            } else if (matrix[row][mid] > target){
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return false;
    
    }
};
