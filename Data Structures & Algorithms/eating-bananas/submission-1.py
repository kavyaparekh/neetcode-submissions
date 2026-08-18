from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kl = 1
        kr = max(piles)
        ans = kr
        

        def possible(kmid, piles):
            time = 0
            for i in range(len(piles)):
                time += ceil(piles[i]/kmid)
            return time


        while kl <= kr:
            kmid = kl + (kr-kl)//2
            if possible(kmid, piles) <= h:
                ans = kmid
                kr = kmid - 1
            else:
                kl = kmid + 1

        return ans