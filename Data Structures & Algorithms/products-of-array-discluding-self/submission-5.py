class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1] * len(nums)
        pre[0] = 1;
        for i in range(1, len(nums)):
             pre[i] = pre[i-1] * nums[i-1];
        

        postt = 1;
        for i in range(len(nums) - 1, -1, -1):            
            pre[i] = pre[i] * postt
            postt = postt * nums[i]

        return pre
        