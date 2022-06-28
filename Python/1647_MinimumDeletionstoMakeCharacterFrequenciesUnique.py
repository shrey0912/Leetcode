class Solution:
    def minDeletions(self, s: str) -> int:
        d={}
        for c in s:
            if not c in d.keys():
                d[c]=1
            else:
                d[c]+=1
        used=set()
        res=0
        for k,f in d.items():
            while f>0 and f in used:
                f-=1
                res+=1
            used.add(f) 
        return res
        
