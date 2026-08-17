class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        vis = set()
        def bt(i, r, c):
            if i == len(word) - 1:
                if board[r][c] == word[-1]:
                    return True
                return False

            vis.add((r,c))

            for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                nr = dr+r
                nc = dc+c
                if 0<=nr<R and 0<=nc<C and (nr,nc) not in vis and board[nr][nc] == word[i+1]:
                    if bt(i+1, nr, nc):
                        return True

            vis.remove((r,c))
            return False

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if bt(0, r, c):
                        return True
        return False
        