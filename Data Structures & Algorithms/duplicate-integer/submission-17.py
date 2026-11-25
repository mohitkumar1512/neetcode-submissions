class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we could use nested loops as a brute force approach. 
        # However this is going to be in O(n^2) so instead we can use sets 

        s_nums = set()
        count = 0
        for num in nums: 
            s_nums.add(num)
            count += 1
        
        return len(s_nums) != count