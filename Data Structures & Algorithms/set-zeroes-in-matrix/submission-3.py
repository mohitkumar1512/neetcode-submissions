class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = False

        # phase 1, mark
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0          # flag the column
                    if r > 0:
                        matrix[r][0] = 0      # flag the row
                    else:
                        first_row_zero = True

        # phase 2, zero the inner cells using the flags
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # phase 3, handle the marker column and row last
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0