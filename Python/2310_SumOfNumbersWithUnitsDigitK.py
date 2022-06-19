class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num==0:
            return 0
        l=[i*k for i in range(1,11)]
        for i in range(len(l)):
            if l[i]%10==num%10:
                if l[i]<=num:
                    return i+1
        return -1

        
