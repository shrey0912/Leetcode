class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ans=0
        cs=list(s)
        i=0
        while i<len(target):
            if target[i] in cs:
                cs.remove(target[i])
                ans+=1
            else:
                break
            if i==len(target)-1:
                i=0
            else:
                i+=1
        return ans//len(target)
