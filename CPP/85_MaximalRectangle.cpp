class Solution {
public:
   int lrh(vector<int> heights)
        {
            vector<int> left;
            stack<pair <int,int>> s;
            int pi=-1;
            for(int i=0;i<heights.size();i++) 
            {
                if(s.size()==0) 
                {
                    left.push_back(pi);
                }
                else if(s.size()>0 && s.top().first<heights[i]) 
                {
                    left.push_back(s.top().second);
                }
                else if(s.size()>0 && s.top().first>=heights[i]) 
                {
                    while(s.size()>0 && s.top().first>=heights[i]) 
                    {
                        s.pop();
                    }
                    if(s.size()==0) 
                    {
                        left.push_back(pi);
                    }
                    else
                    {
                        left.push_back(s.top().second);
                    }
                }   
                s.push({heights[i],i});
              }
            vector<int> right;
            stack<pair <int,int>> sr;
            pi=heights.size();
            for(int i=heights.size()-1;i>=0;i--)  
            {
                if(sr.size()==0) 
                {
                    right.push_back(pi);
                }
                else if(sr.size()>0 && sr.top().first<heights[i]) 
                {
                    right.push_back(sr.top().second);
                }
                else if(sr.size()>0 && sr.top().first>=heights[i]) 
                {
                    while(sr.size()>0 && sr.top().first>=heights[i]) 
                    {
                        sr.pop();
                    }
                    if(sr.size()==0) 
                    {
                        right.push_back(pi);
                    }
                    else
                    {  
                        right.push_back(sr.top().second);
                    }
                }
                sr.push({heights[i],i});
            }
            reverse(right.begin(),right.end());
            vector<int> area;
            int maxarr=0;
            for(int i=0;i<heights.size();i++) 
            {
                int temparr=(right[i]-left[i]-1)*heights[i];
                if(temparr>maxarr) 
                {
                    maxarr=temparr;
                }
            }
            return maxarr;
        }
    int maximalRectangle(vector<vector<char>>& matrix) {
        int n=matrix.size();
        int m=matrix[0].size();
        vector<vector<int>> mf(n,vector<int> (m,0));
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                mf[i][j]=matrix[i][j]-48;
            }
        }
        int mr=lrh(mf[0]);
        for(int i=1;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(mf[i][j]!=0)
                {
                    mf[i][j]+=mf[i-1][j];
                }
            }
            int clrh=lrh(mf[i]);
            if(clrh>mr)
            {
                mr=clrh;
            }
        }
        return mr;
    }
};
