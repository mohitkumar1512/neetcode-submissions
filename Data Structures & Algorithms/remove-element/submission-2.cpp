class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        /*
        1 1 2 3 4 

        */
         int n = nums.size();
        nums.erase(remove(nums.begin(), nums.end(), val), nums.end());
        return nums.size();

    }
};