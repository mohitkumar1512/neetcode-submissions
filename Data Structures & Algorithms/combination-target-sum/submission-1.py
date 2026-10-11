class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i, total):
            if total == target:
                res.append(path[:])
                return
            if i >= len(nums) or total > target:
                return

            path.append(nums[i])
            backtrack(i, total + nums[i])     # reuse same number
            path.pop()

            backtrack(i + 1, total)           # move to next number

        backtrack(0, 0)
        return res