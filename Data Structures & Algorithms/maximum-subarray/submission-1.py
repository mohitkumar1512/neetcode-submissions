class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #sliding window 
        max_sum = float('-inf')
        curr = 0
        for r in range(len(nums)):
            curr += nums[r]
            max_sum = max(max_sum, curr)
            if curr <= 0: curr = 0
        return max_sum
            