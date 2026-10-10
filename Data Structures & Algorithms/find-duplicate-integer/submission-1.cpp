class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = 0, fast = 0;

        while (true){
            slow = nums[slow];
            fast = nums[nums[fast]];

            if (slow == fast) break;
        }    
        int another_slow = 0;
        
        while (true){
            slow = nums[slow];
            another_slow = nums[another_slow];

            if (another_slow == slow) return slow;
    }}
};
