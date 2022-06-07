class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.pop()
        for b in nums2:
            t=len(nums1)-1
            while t>=0 and b<nums1[t]:
                t-=1
            nums1.insert(t+1,b) 
