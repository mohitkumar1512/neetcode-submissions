class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // int res  = nums.size();
        // for (int i = 0; i < nums.size(); i++){
        //     res += (i - nums[i]);
        // }
        // return res;

        int res = nums.size(); // start with n (last index not in loop)

        for (int i = 0; i < nums.size(); i++) {
            res ^= i ^ nums[i]; // XOR both index and value
        }

        return res;
    }
};
