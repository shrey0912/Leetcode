class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l=[]
        for i in range(len(number)):
            if number[i]==digit:
                l.append(int(number[:i]+number[i+1:]))
        return str(max(l))
