class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)!=1:
            c=[]
            for i in range(len(nums)-1):
                c.append((nums[i]+nums[i+1])%10)
            nums=c
        return nums[0]
