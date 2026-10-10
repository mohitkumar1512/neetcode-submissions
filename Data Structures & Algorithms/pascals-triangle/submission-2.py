class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Build a pascal triangle
        # Can we recurse? 
        # rows start from 1 - n in terms of size
        # first always one second always 1, 1
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res