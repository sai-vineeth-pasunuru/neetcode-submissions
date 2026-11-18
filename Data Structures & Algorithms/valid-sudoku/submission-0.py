class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = board[i]
            numbers = [x for x in row if x != "."]
            if len(numbers) != len(set(numbers)):
                return False 

        for j in range(len(board)):
            column = []
            for i in range(len(board)):
                if board[i][j] != '.':
                    column.append(board[i][j])
            if len(column) != len(set(column)):
                return False 


        for i in range(0,9,3):
            for j in range(0,9,3):

                box = [board[i][j], board[i][j+1], board[i][j+2], board[i+1][j], board[i+1][j+1], board[i+1][j+2], board[i+2][j], board[i+2][j+1], board[i+2][j+2]]
                nonzero = [x for x in box if x != "."]
                if len(nonzero) != len(set(nonzero)):
                    return False 

        return True