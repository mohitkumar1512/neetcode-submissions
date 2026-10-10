class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // two pointer approach
        // twoSum = {}
        // for i in range(len(nums)):
        //     if len(twoSum):
        //         diff = target - nums[i]
        //         if diff in twoSum:
        //             return [twoSum[diff], i]
            
        //     twoSum[nums[i]] = i
        
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
