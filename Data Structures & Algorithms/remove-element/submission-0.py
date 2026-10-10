class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        lenNums = len(nums) - 1
        while index <= lenNums:
            # print(nums[index])
            if nums[index] == val:
                lenNums -= 1
                del nums[index]
            else:
                index += 1
        return len(nums)