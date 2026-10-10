class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incre = 1
        decre = 1
        longest = 1 
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                incre += 1
                decre = 1  # not 0
            elif nums[i] < nums[i - 1]:
                decre += 1
                incre = 1  # not 0
            else:
                incre = decre = 1  # equal -- reset both, you're missing this case too
            longest = max(longest, incre, decre)
        return longest