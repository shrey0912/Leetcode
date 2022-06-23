class Solution:

    def greatestLetter(self, s: str) -> str:

        d={}

        for t in s:

            if t.upper() not in d.keys():

                d[t.upper()]=[t]

            else:

                d[t.upper()].append(t)

        for e in sorted(d,reverse=True):

            if len(set(d[e]))==2:

                return e

        return ''

        

                

        
