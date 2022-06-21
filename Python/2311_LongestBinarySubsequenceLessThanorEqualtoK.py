class Solution:

    def longestSubsequence(self, s: str, k: int) -> int:

        ans=len(s)

        val=0

        for i in range(len(s)):

            val+=int(s[i])*(2**(len(s)-i-1))

        for i in range(len(s)):

            if val<=k:

                    return ans

            if s[i]=='1':

                ans-=1

                val-=int(s[i])*(2**(len(s)-i-1))

        return ans

            

            

        
