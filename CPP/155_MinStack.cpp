class MinStack {
private:
    stack<int> s;
    stack<int> ss;
public:  
    void push(int val) {
        s.push(val);
        if(ss.size()==0 or val<=ss.top())
            {
            ss.push(val);
        }
        return;
    }
    
    int pop() {
        int ans=s.top();
        s.pop();
        if(ans==ss.top()) 
            {
            ss.pop();
        }
        return ans;
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return ss.top();
    }
};
