class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxAreaContainer = 0
        while left < right:
            lowest = min(heights[left], heights[right])
            maxAreaContainer = max((right - left) * lowest, maxAreaContainer)

            if lowest == heights[left]:
                left += 1
            else:
                right -= 1 

        return maxAreaContainer