class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        s=list(s)
        num=s.count(letter)
        den=len(s)
        return int(num/den*100)
