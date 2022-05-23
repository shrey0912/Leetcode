class Solution:
    def trap(self, height: List[int]) -> int:
        lmx=[]
        rmx=[]
        lmx.append(height[0]) 
        rmx.append(height[-1]) 
        for i in range(1,len(height)):
            lmx.append(max(lmx[i-1],height[i])) 
        for i in range(len(height)-2,-1,-1):
                       rmx.insert(0,max(rmx[0],height[i])) 
        res=[]
        for i in range(len(height)):
                       res.append(min(lmx[i],rmx[i])-height [i]) 
        print(res) 
        return sum(res) 
       
        
