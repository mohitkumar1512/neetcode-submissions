class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force
        # output = []
        # nums.sort()
        # for i in range (len(nums)):
        #     for j in range (i + 1, len(nums)):
        #         for k in range (j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                     output.append([nums[i], nums[j], nums[k]])      
        
        # output = list(set(tuple(x) for x in output))
        # output = [list(x) for x in output]

        # return output

        # optimize using 2 sum approach
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if num + nums[left] + nums[right] == 0:
                    output.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif num + nums[left] + nums[right] < 0:
                    left += 1
                
                else:
                    right -= 1

        return output




