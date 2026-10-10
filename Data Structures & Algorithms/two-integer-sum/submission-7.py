class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # brute force
        # # worst case this has O(n^2) complexity
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums [j] == target:
        #             return [i,j]

        # return []

        # optimize using two sum approach
        twoSum = {}
        for i in range(len(nums)):
            if len(twoSum):
                diff = target - nums[i]
                if diff in twoSum:
                    return [twoSum[diff], i]
            
            twoSum[nums[i]] = i


