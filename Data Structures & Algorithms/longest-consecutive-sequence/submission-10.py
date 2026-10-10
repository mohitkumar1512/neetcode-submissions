class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s_nums = set(nums)
        for num in nums:
            if num - 1 not in s_nums:
                curr = num
                running = 0
                while curr in s_nums:
                    running += 1
                    curr += 1
                
                longest = max(running, longest)
        return longest