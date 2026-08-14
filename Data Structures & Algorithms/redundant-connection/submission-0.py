class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        Parent = [i for i in range(n+1)]
        Rank = [0]*(n+1)

        def find(A):
            if Parent[A] == A:
                return A
            Parent[A] = find(Parent[A])
            return Parent[A]
        
        def union(A, B):
            pA = find(A)
            pB = find(B)

            if pA == pB:
                return False
            
            if Rank[pA]==Rank[pB]:
                Parent[pB] = pA
                Rank[pA] += 1
            elif Rank[pA] > Rank[pB]:
                Parent[pB] = pA
            else:
                Parent[pA] = pB

            return True
        
        for A, B in edges:
            if not union(A, B):
                return [A, B]