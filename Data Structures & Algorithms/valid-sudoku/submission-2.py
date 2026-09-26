class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R, C = len(board), len(board[0])
        # rows = set()
        # for row in board:
        #     for r in row:
        #         if r == ".":
        #             continue
        #         if r not in rows:
        #             rows.add(int(r))
        #         else:
        #             return False
        #     rows.clear()
        
        rows = set()
        for r in range(R):
            for c in range(C):
                if board[r][c] == ".":
                    continue
                if int(board[r][c]) not in rows:
                    rows.add(int(board[r][c]))
                else:
                    return False
            rows.clear()

        cols = set()
        for c in range(C):
            for r in range(R):
                if board[r][c] == ".":
                    continue
                if int(board[r][c]) not in cols:
                    cols.add(int(board[r][c]))
                else:
                    return False
            cols.clear()

        hs = {
            (0,0) : set(),
            (0,1) : set(),
            (0,2) : set(),
            (1,0) : set(),
            (1,1) : set(),
            (1,2) : set(),
            (2,0) : set(),
            (2,1) : set(),
            (2,2) : set()
        }

        for r in range(R):
            for c in range(C):
                if board[r][c] == ".":
                    continue
                if int(board[r][c]) in hs[(r//3, c//3)]:
                    return False
                else:
                    hs[(r//3, c//3)].add(int(board[r][c]))
                    
        return True
