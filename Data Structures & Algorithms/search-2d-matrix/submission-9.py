class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0 
        bottom = len(matrix) - 1
        
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom: 
            m = (top + bottom) // 2
            if matrix[m][right] >= target >= matrix[m][left]:
                while left <= right: 
                    mid = (left + right) // 2
                    if matrix[m][mid] == target:
                        return True
                    elif matrix[m][mid] > target: 
                        right = mid - 1
                    else:
                        left = mid + 1
            elif matrix[m][left] > target:
                bottom = m - 1
            else:
                top = m + 1
        
        return False