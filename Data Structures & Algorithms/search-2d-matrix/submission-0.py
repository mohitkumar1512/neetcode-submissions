class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        target_arr = []
        while left <= right:
            mid = (left + right) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid])-1]:
                target_arr =  matrix[mid]
                break
            elif target >= matrix[mid][len(matrix[mid])-1]:
                left = mid + 1
            elif target <= matrix[mid][len(matrix[mid])-1]:
                right = mid - 1

        if target_arr and target in target_arr:
            return True
        return False
            
