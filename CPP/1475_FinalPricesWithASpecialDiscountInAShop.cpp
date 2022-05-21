class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        vector<int> v;
        stack<int> s;
        for(int i=prices.size()-1;i>=0;i--) 
        {
            if(s.size()==0) 
            {
                v.push_back(-1);
            }
            else if(s.size()>0 && s.top()<=prices[i])
            {
                v.push_back(s.top());
            }
            else if(s.size()>0 && s.top()>prices[i]) 
            {
                while(s.size()>0 && s.top()>prices[i]) 
                {
                    s.pop();
                }
                if(s.size()==0) 
                {
                    v.push_back(-1);
                }
                else
                {
                    v.push_back(s.top());
                }
            }
            s.push(prices[i]);
        }
        reverse(v.begin(),v.end());
        for(int i=0;i<prices.size();i++) 
        {
            if(v[i]!=-1) 
            {
                prices[i]-=v[i];
            }
        }
        return prices;
 }
};
