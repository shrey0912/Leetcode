class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dw={}
        dl={}
        for m in matches:
            if m[0] not in dw.keys():
                dw[m[0]]=1
            else:
                dw[m[0]]+=1
            if m[1] not in dl.keys():
                dl[m[1]]=1
            else:
                dl[m[1]]+=1
        a=set(dw.keys()).difference(set(dl.keys()))
        b=[l for l in dl.keys() if dl[l]==1]
        return [sorted(a),sorted(b)]
