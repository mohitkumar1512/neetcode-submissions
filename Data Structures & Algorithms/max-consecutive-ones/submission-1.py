class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        tempV = 0
        for num in nums: 
            if num == 1: tempV += 1
            else: tempV = 0 
            result = max(tempV, result)
            
        return result