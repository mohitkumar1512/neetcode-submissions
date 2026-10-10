class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        map_nums = defaultdict(int)
        n = len(nums)
        nums.sort()
        res = []

        # -4, -1, -1, 0, 1, 2
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            num = nums[i]
            
            l = i + 1
            r = n - 1
            while l < r: 
                total = num + nums[l] + nums[r]
                if total == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total < 0:
                    l += 1
                else: 
                    r -= 1
        return res

            