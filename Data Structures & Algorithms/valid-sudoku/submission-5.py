class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        col_seen = {}

        for i in range(9):
            col_seen[i] = {}

        for row in range(len(board)):
            row_seen={}
            for c_index_ in range(len(board[row])):
                if board[row][c_index_]!= "." and (board[row][c_index_] in row_seen or board[row][c_index_] in col_seen[c_index_]):
                    return False
                row_seen[board[row][c_index_]] = True
                col_seen[c_index_][board[row][c_index_]] = True
        

        for x in range(3):
            for y in range(3):
                seen = {}
                for j in range(x*3,3+x*3):
                    for k in range(y*3,3+y*3):
                        if board[j][k] != "." and board[j][k] in seen:
                            return False
                        seen[board[j][k]] = True

            
                


        return True

        