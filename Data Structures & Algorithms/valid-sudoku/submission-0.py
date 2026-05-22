class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows for dups
        for row in board:
            digits = [x for x in row if x != "."]
            if len(digits) != len(set(digits)):
                return False

        # Check cols for dups
        for col in range(9):
            digits = [board[row][col] for row in range(9) if board[row][col] != "."]
            if len(digits) != len(set(digits)):
                return False
        # Check 3x3 for dups
        for c in range(0,9,3):
            for r in range(0,9,3):
                lst = []
                lst.append(board[c][r])
                lst.append(board[c][r + 1])
                lst.append(board[c][r + 2])
                lst.append(board[c + 1][r])
                lst.append(board[c + 1][r + 1])
                lst.append(board[c + 1][r + 2])
                lst.append(board[c + 2][r])
                lst.append(board[c + 2][r + 1])
                lst.append(board[c + 2][r + 2])
                digits = [x for x in lst if x != "."]
                if len(digits) != len(set(digits)):
                    return False
        
        return True