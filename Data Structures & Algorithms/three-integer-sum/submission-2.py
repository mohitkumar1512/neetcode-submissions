class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force
        output = []
        nums.sort()
        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                for k in range (j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                            output.append([nums[i], nums[j], nums[k]])      
        
        output = list(set(tuple(x) for x in output))
        output = [list(x) for x in output]

        return output