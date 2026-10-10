class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flat = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))]
        dup = missing = -1
        
        for val in flat:
            idx = abs(val) - 1
            if flat[idx] < 0:
                dup = abs(val)
            else:
                flat[idx] *= -1
        
        for i in range(len(flat)):
            if flat[i] > 0:
                missing = i + 1
        
        return [dup, missing]
        