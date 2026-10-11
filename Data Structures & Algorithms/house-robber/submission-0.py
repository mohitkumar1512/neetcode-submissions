class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n == 1:
        #     return nums[0]

        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, n):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # return dp[-1]

        prev2, prev1 = 0, 0  # best at i-2, best at i-1
        for x in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1