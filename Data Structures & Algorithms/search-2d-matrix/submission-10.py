class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        up, down = 0, rows - 1
        while up <= down:
            center = (up + down) // 2
            if matrix[center][0] <= target <= matrix[center][cols - 1]:
                l, r = 0, cols - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[center][m] == target:
                        return True
                    elif matrix[center][m] > target:
                        r = m - 1
                    else:
                        l = m + 1
                return False
            elif matrix[center][cols - 1] < target:
                up = center + 1
            else:
                down = center - 1
        return False