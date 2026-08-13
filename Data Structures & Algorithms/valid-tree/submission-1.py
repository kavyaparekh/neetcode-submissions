class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        Parent = []
        Rank = []
        Parent = [i for i in range(n)]
        Rank = [0]*n
        
        def Find(A):
            if Parent[A] == A:
                return A
            Parent[A] = Find(Parent[A])
            return Parent[A]

        def Union(A, B):
            pA = Find(A)
            pB = Find(B)

            if pA == pB:
                return False
            if Rank[pA] == Rank[pB]:
                Parent[pB] = pA
                Rank[pA] += 1
            elif Rank[pA] > Rank[pB]:
                Parent[pB] = pA
            else:
                Parent[pA] = pB
            return True

        for A, B in edges:
            if not Union(A, B):
                return False
        return True

        