class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        paran = []
        def backtracking(openN, closeN):
            if openN == closeN == n:
                res.append("".join(paran))
                return
            
            if openN < n:
                paran.append("(")
                backtracking(openN+1, closeN)
                paran.pop()
            
            if closeN < openN:
                paran.append(")")
                backtracking(openN, closeN+1)
                paran.pop()
        
        backtracking(0,0)
        return res
