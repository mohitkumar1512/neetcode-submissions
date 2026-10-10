class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;

        while (left < right){
            if (numbers[right] + numbers[left] == target){
                return {left + 1, right + 1};
            }
            if (numbers[right] + numbers[left] > target){
                right -= 1;
            }
            if (numbers[right] + numbers[left] < target){
                left += 1;
            }
        }
        
    }
};
