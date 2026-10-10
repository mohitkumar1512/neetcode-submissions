class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: continue 
            l = i + 1
            r = len(nums) - 1
            while l < r: 
                threeS = a + nums[l] + nums[r]
                if threeS == 0: 
                    res.append([a, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                            l += 1
                    while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                    l += 1
                    r -= 1
                elif threeS < 0:
                    l += 1
                else: r -= 1

        return res
                