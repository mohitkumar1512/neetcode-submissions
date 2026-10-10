class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        n = len(nums) 
        for key, value in hashMap.items():
            if value >= n // 2:
                return key
        