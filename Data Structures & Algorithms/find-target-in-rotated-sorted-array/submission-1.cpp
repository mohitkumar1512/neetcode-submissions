class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        /*
        at each mid, one half is always sorted.

        if nums[l] <= nums[mid]:        → left half is sorted
            if target is within [l, mid]:   → go left
                r = mid - 1
            else:                           → go right
                l = mid + 1

        else:                           → right half is sorted
            if target is within [mid, r]:   → go right
                l = mid + 1
            else:                           → go left
                r = mid - 1
        
        */
        int l = 0; 
        int r = nums.size() - 1;

        while (l <= r){
            int m = l  + (r - l) / 2;
            if (nums[m] == target){
                return m;
            } else if (nums[l] <= nums[m]){
                if (target >= nums[l] && target < nums[m]){
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            } else {
                if (target <= nums[r] && target > nums[m]){
                    l = m + 1;
                } else {
                    r = m - 1;
                } 
            }
        }
        return -1;
    }
};
