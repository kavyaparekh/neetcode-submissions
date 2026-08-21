class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height)-1
        lMax = height[l]
        rMax = height[r]
        res = 0
        
        while l<r:
            if lMax < rMax:
                l+=1
                lMax = max(height[l],lMax)
                res += lMax-height[l] 
            else:
                r-=1
                rMax = max(height[r], rMax)
                res+= rMax-height[r]
                
        return res