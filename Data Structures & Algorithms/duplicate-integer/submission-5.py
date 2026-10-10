class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        count = {}
        for num in nums:
            if count.get(num): 
                return True
            count[num] = 1
        return False


        


            

