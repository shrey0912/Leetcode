class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        lcs=[[-1 for i in range(n+1)]for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    lcs[i][j]=0
                elif word1[i-1]==word2[j-1]:
                    lcs[i][j]=1+lcs[i-1][j-1]
                else:
                    lcs[i][j]=max(lcs[i-1][j], lcs[i][j-1]) 
                    
        cw=lcs[m][n] 
    
        return m-cw+n-cw
