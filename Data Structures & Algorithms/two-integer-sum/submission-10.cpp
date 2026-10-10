class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {        
        unordered_map<int, int> mt;
        for (int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if (mt.count(diff)){
                return {mt[diff], i};
            }
            mt[nums[i]] = i;
        }
        
    }
};
