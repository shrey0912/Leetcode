class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        c=[inf, -inf]
        for n in nums:
            d=abs(n)
            if d<c[0]:
                c=[d,n]
            if d==c[0]:
                if n>c[1]:
                    c=[d,n]
        return c[1]
