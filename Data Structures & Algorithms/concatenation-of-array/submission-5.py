class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len  = len(nums)
        ans = [0] * 2 * nums_len

        for idx in range(len(nums)):
            ans[idx] = nums[idx]
            ans[idx+nums_len] = nums[idx]

        return ans