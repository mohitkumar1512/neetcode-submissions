class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = nums[0];
        int curr_sum = 0;
    
        for (int right = 0; right < nums.size(); right++){
            if (curr_sum < 0) curr_sum = 0;
            curr_sum += nums[right];
            sum = max(sum, curr_sum);

        }
        return sum;
    }
};
