class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int>x;
        int i=0,res=0;
        x.push(-1);
        while(i<s.length()){
            if(s[i]=='(') x.push(i);
            else{
                if(!x.empty()) x.pop();
                if(!x.empty()) {
                    res=max(res,i-x.top());
                }
                else x.push(i);
            }
            i++;
        }
        return res;
    }
};