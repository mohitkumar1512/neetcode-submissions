class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s_nums = set(nums)
        seen = set()
        for num in nums:
            running = 0
            curr = num
            if num not in seen:
                while curr in s_nums:
                    running += 1
                    seen.add(curr)
                    curr += 1
                
            longest = max(running, longest)
        return longest