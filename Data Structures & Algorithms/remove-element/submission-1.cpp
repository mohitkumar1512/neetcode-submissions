class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        /*
        1 1 2 3 4 

        */
        int i = 0, n = nums.size();
        while (i < n) {
            if (nums[i] == val) {
                nums[i] = nums[--n];
            } else {
                i++;
            }
        }
        return n;
    }
};