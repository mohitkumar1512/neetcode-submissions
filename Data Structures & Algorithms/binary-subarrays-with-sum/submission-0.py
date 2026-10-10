class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Never going to go to a smaller number
        def helper(x):
            if x < 0: return 0

            res = 0
            l, curr_total = 0, 0
            for r in range(len(nums)):
                curr_total += nums[r]
                while curr_total > x: 
                    curr_total -= nums[l]
                    l += 1
                res += (r - l + 1)
                
            return res

        return helper(goal) - helper(goal - 1)