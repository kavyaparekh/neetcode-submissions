class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        qA = deque()
        qP = deque()
        visA = set()
        visP = set()

        def bfs(q, vis):
            while q:
                r, c = q.popleft()
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr,nc = dr+r, dc+c
                    if 0<=nr<R and 0<=nc<C and heights[nr][nc] >= heights[r][c]and (nr,nc) not in vis:
                        q.append((nr,nc))
                        vis.add((nr,nc))

            return vis

        for r in range(R):
            for c in range(C):
                if r==0 or c==0:
                    qP.append((r,c))
                    visP.add((r,c))
                if r==R-1 or c==C-1:
                    qA.append((r,c))
                    visA.add((r,c))
    
        visA = bfs(qA, visA)
        visP = bfs(qP, visP)

        return list(visA & visP)