class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d={}
        for i in range(n):
            d[i]=0
        for r in roads:
            d[r[0]]+=1
            d[r[1]]+=1
        sd=sorted(d,key=d.get,reverse=True)
        d2={}
        m=n
        for s in sd:
            d2[s]=m
            m-=1
        imp=0
        for r in roads:
            imp+=d2[r[0]]+d2[r[1]]
        return imp
