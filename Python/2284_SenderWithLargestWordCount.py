class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d={}
        for s in set(senders):
            d[s]=[0]
        for i in range(len(messages)):
            msg=messages[i].split(' ')
            d[senders[i]][0]+=len(msg)
        mw=max(d.values())
        mwl=[]
        for k,v in d.items():
            if v==mw:
                mwl.append(k)
        mwl.sort(reverse=True)
        return mwl[0]
        
