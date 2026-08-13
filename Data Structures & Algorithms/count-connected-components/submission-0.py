class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        Parent = [i for i in range(n)]
        Rank = [0]*n
        count = n

        def find(A):
            if Parent[A] == A:
                return A
            Parent[A] = find(Parent[A])
            return Parent[A]
        
        def union(A, B):
            nonlocal count
            pA = find(A)
            pB = find(B)

            if pA == pB:
                return
            if Rank[pA] == Rank[pB]:
                Parent[pB] = pA
                Rank[pA] += 1
            elif Rank[pA] > Rank[pB]:
                Parent[pB] = pA
            else:
                Parent[pA] = pB
            
            count -= 1
        

        for A, B in edges:
            union(A, B)
        
        return count
        