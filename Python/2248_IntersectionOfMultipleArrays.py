class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d={}
        for i in range(1001):
            d[i]=0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[nums[i][j]]+=1
        l=[]
        for k,v in d.items():
            if v==len(nums):
                l.append(k)
        return l
