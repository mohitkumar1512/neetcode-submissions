class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCount = {}
        for num in nums: 
            numCount[num] = numCount.get(num, 0) + 1
            if (numCount[num]) > 1: return True
        return False


        


            

