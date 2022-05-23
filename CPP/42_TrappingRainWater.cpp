class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> lmx;
        vector<int> rmx;
        lmx.push_back(height[0]);
        for(int i=1;i<height.size();i++) 
            {
            lmx.push_back(max(lmx[i-1],height[i])) ;
        }
        rmx.push_back(height[height.size()-1]);
        int t=1;
        for(int i=height.size()-2;i>=0;i--) 
            {
            rmx.push_back(max(rmx[t-1],height[i]));
            t++;
        }
        reverse(rmx.begin(),rmx.end());
        int ans=0;
        for(int i=0;i<height.size();i++) 
            {
            ans+=min(lmx[i],rmx[i])-height[i];
        }
        return ans;
    }
};
