class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        n=0
        for w in words:
            if s.startswith(w):
                n+=1
        return n
