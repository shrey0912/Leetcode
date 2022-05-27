class Solution {
public:
    int numberOfSteps(int num) {
        int nos=0;
        if(num==0)
        {
            return nos;
        }
        else if(num%2==0)
        {
            return nos+1+numberOfSteps(num/2);
        }
        else
        {
            return nos+1+numberOfSteps(num-1);
        }
        return nos;
    }
};
