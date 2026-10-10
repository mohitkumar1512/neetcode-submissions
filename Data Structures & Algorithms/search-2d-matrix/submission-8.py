class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left_r = 0
        right_r = rows - 1

        while left_r <= right_r: 
            mid = (left_r + right_r) // 2
            if matrix[mid][0] <= target and matrix[mid][cols - 1] >= target: 
                left_c = 0
                right_c = cols - 1
                while left_c <= right_c: 
                    mid_c = (left_c + right_c) // 2
                    if matrix[mid][mid_c] == target: 
                        return True
                    elif matrix[mid][mid_c] > target: 
                        right_c = mid_c - 1
                    else: 
                        left_c = mid_c + 1
                return False

            elif matrix[mid][cols - 1] > target:
                right_r = mid - 1
            else: left_r = mid + 1
        
        return False