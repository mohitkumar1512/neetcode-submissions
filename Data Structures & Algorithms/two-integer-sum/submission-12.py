class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if seen.get(num):
                return [seen[num] - 1, i]
            seen[target-num] = i + 1
        
