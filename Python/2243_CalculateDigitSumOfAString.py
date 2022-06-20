class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            n=''
            cs=0
            for i in range(len(s)):
                cs+=int(s[i])
                if (i+1)%k==0 or i==len(s)-1:
                    n+=str(cs)
                    cs=0
            s=n
        return s
                    
                
                
        
