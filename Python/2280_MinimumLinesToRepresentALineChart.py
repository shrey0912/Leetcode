class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if(len(stockPrices)==1):
            return 0
        stockPrices.sort()
        gslope=inf
        lines=1
        for i in range(1,len(stockPrices)-1):
            one=(stockPrices[i][1]-stockPrices[i-1][1])*(stockPrices[i+1][0]-stockPrices[i][0])
            two=(stockPrices[i+1][1]-stockPrices[i][1])*(stockPrices[i][0]-stockPrices[i-1][0])
            if one!=two:
                lines+=1
        return lines
