class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ls=[]
        for i in range(len(s)+1-k):
            ss=s[i:i+k]
            ls.append(ss)
        return len(set(ls))==2**k
