class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = {r:set() for r in range(9)}
        colSet = {c:set() for c in range(9)}
        squareSet = {s:set() for s in range(9)}

        for r, row in enumerate(board):
            for c, col in enumerate(row):
                squareInd = (r // 3) * 3 + (c // 3)
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in rowSet[r] 
                    or board[r][c] in colSet[c]
                    or board[r][c] in squareSet[squareInd]):
                    return False
                else:
                    rowSet[r].add(board[r][c])
                    colSet[c].add(board[r][c])
                    squareSet[squareInd].add(board[r][c])
        return True
