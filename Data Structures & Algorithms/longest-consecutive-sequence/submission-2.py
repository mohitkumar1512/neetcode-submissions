class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}
        if len(nums) == 1:
            return 1
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        
        maxSequence = 0
        for num in nums:
            if (num - 1) not in hashMap:
                start = num
                seq = 0
                while start in hashMap:
                    seq += 1
                    start += 1
                maxSequence = max(maxSequence, seq)

        return maxSequence