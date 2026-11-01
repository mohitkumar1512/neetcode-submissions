class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def mark(r, c):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                    board[r][c] = 'S'
                    for dr, dc in DIRS:
                        stack.append((r + dr, c + dc))
        
                # 1. mark safe cells starting from the border
        for r in range(rows):
            mark(r, 0)
            mark(r, cols - 1)
        for c in range(cols):
            mark(0, c)
            mark(rows - 1, c)

        # 2 + 3. capture surrounded, restore safe
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'