class Solution {
public:
    int majorityElement(vector<int>& nums) {
        long cand = 0;
        int count = 0;

        for (auto num : nums){
            if (count == 0){
                cand = num;
            }
            
            if (num == cand){
                count += 1;
            }
            else{
                count -= 1;
            }
        }
        return cand;
    }
};