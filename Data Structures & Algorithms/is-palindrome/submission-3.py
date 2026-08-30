class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newStr = ""
        for i in range(len(s)):
            if s[i].isalnum():
                newStr += s[i].lower()
        print(newStr)
        
        l, r = 0, len(newStr)-1
        while l < r:
            if newStr[l]==newStr[r]:
                l+=1
                r-=1
                continue
            else:
                return False
        
        return True
            