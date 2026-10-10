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

        left = 0
        right = len(target_arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if target_arr[mid] == target:
                return True
            elif target_arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
            
