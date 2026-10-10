class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        for l in range(len(nums)):
            leftSum += nums[l]
            
            if leftSum == rightSum: return l
            
            rightSum -= nums[l]

        return -1 