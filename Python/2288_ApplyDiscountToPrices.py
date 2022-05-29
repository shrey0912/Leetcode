class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        s=sentence.split(' ')
        print(s)
        ase=[]
        for se in s:
            if se[0]=='$' and len(se)>1:
                if not se[1:].isdigit():
                    ase.append(se)
                    continue
                p=int(se[1:])
                p-=(discount*p)/100
                p='{0:.2f}'.format(p)
                ase.append('$'+str(p))
            else:
                ase.append(se)
        return ' '.join(ase)
                
        
