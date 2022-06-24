class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans=[]
        for q in queries:
            ans.append(0)
            for p in points:
                dc=(p[0]-q[0])**2+(p[1]-q[1])**2
                if dc<=q[2]**2:
                    ans[-1]+=1
        return ans
        
