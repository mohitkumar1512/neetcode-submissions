class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++){
            if (i > 0 && nums[i] == nums[i-1]) continue;
            
            int left = i + 1;
            int right = nums.size() - 1;
            
            
            while (left < right){
                if (nums[i] + nums[left] + nums[right] == 0){
                    res.push_back({nums[i], nums[left], nums[right]});
                    left += 1;
                    right -= 1;
                    while (left < right and nums[left] == nums[left-1]) left += 1;
                    while (left < right and nums[right] == nums[right+1]) right -= 1;
                } 
                else if (nums[i] + nums[left] + nums[right] < 0) left += 1;
                else right -= 1;
            }
        }
        return res;
    }
};
