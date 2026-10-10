class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        m_area = 0
        while l < r: 
            m_area = max(m_area, (r - l) * min(heights[l], heights[r]))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return m_area
