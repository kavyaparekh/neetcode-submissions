class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        top = 0
        bottom = R - 1

        while top<=bottom:
            midRow = top + (bottom-top)//2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bottom = midRow - 1
            else:
                break
                
        if not top<=bottom:
            return False

        midRow = top + (bottom-top)//2
        l = 0 
        r = C-1
        
        while l<=r:
            mid = l+(r-l)//2
            if target == matrix[midRow][mid]:
                return True
            elif target > matrix[midRow][mid]:
                l = mid+1
            elif target < matrix[midRow][mid]:
                r = mid-1
            
        return False
            

            
            
            

