class Solution {
public:
    vector<vector<int>> res;
    vector<int> curr;
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        // we need a res array
        // we need to maintain which elements we are allowed to choose from
        // we need to dfs through the entire array
        // we need a total (for target sum) 
        // -- if we go over we return 
        dfs(nums, target, 0, 0);
        return res;

    }
    void dfs(vector<int>& nums, int target, int i, int totl){
        if (totl == target) {
            res.push_back(curr);
            return;
        }
        if (i >= nums.size() || totl > target) return;
        curr.push_back(nums[i]);
        dfs(nums, target, i, totl + nums[i]);
        curr.pop_back();
        dfs(nums, target, i+1, totl);
    }
};
