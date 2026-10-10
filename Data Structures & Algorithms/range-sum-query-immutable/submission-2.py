class NumArray:
    
    

    def __init__(self, nums: List[int]):
        self.value = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.value[i+1] = self.value[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.value[right+1] - self.value[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)