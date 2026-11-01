class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in mapp: 
                return [mapp[diff], index]
            mapp[num] = index
