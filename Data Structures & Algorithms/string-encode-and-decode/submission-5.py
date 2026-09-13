class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= str(len(s))+"#"+s  
          
        return res

    def decode(self, s: str) -> List[str]:
        ans = []
        i=0
        while i < len(s):
             
            strs = ""
            num = ""
            while s[i]!="#":
                num += s[i]
                i+=1
             
            k = int(num)
             
             
            for j in range(i+1,i+k+1):
                strs += s[j]
           
            ans.append(strs)
            i = i+k+1

        return ans
                

