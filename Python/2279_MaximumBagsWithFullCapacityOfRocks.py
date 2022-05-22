class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remcap=[capacity[i]-rocks[i] for i in range(len(rocks))]
        remcap.sort()
        fill=0
        tot=0
        for r in remcap:
            if fill+r<=additionalRocks:
                fill+=r
                tot+=1
        return tot
        
