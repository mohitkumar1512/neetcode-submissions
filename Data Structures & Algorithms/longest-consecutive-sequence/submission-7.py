class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_s = 0
        for num in num_set: 
            if num - 1 not in num_set:
                seq = 1
                curr = num + 1
                while curr in num_set: 
                    seq += 1
                    curr += 1
                max_s = max(seq, max_s)
        
        return max_s