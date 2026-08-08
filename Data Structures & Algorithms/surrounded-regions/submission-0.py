class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        q = deque()

        def bfs():
            while q: 
                r, c = q.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 'O':
                        board[nr][nc] = 'T'
                        q.append((nr, nc))

        
        for r in range(R):
            for c in range(C):
                if (r == 0 or r == R-1 or c == 0 or c == C-1) and board[r][c] == 'O':
                    board[r][c] = 'T'
                    q.append((r,c))
        
        bfs()

        for r in range(R):
                for c in range(C):
                    if board[r][c] == 'O':
                        board[r][c] = 'X'
                    elif board[r][c] == 'T':
                        board[r][c] = 'O'




