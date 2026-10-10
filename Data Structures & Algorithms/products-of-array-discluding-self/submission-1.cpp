class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        long prod = 1;
        vector<int> pre;
        vector<int> post;
        for(int i = 0; i < nums.size(); i++ ){
            pre.push_back(prod);
            prod *= nums[i];
        }
        prod = 1;
        for(int i = nums.size() - 1; i >= 0; i-- )
        {
            post.push_back(prod);
            prod *= nums[i];
        }
        long index = nums.size() - 1;
        for(int i = 0; i < nums.size(); i++){
            pre[i] *= post[index];
            index -= 1;
        }
        return pre;
    }
};
