class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> mn;
        if (nums.size() == 1)
            {return 1;}
        
        for (int i = 0; i < nums.size(); i++){
            mn.insert(nums[i]);
        }
        long maxS = 0;
        for (auto num: nums){
            if (!mn.count(num - 1)){    
                int start = num;
                long seq = 0;
                while (mn.count(start)){
                    seq += 1;
                    start += 1;
                }
                maxS = max(maxS, seq);
            } 
        }
        
        
        return maxS;
    }
};
