class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[[],[]]
        a=set(nums1).difference(set(nums2)) 
        b=set(nums2).difference(set(nums1))
        ans[0]=list(a) 
        ans[1]=list(b) 
        return ans
        
