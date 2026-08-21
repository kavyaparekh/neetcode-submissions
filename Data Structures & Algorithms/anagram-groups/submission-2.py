class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)
        res = []
        for word in strs:
            sign = [0]*26
            for ch in word:
                sign[ord(ch)-ord('a')] += 1
            mp[tuple(sign)].append(word)

        for val in mp.values():
            res.append(val)
        
        return res