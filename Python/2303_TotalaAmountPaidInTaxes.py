class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax=0.0
        ci=0
        for i in range(len(brackets)-1,0,-1):
            brackets[i][0]-=brackets[i-1][0]
        for i in range(len(brackets)):
            if brackets[i][0]+ci<=income:
                tax+=float(brackets[i][0])*(brackets[i][1])/100
                if brackets[i][0]+ci==income:
                    break
                ci+=brackets[i][0]
            else:
                tax+=float(income-ci)*(brackets[i][1])/100
                break
        return tax
